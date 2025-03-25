# ruff: noqa: F401
from collections.abc import AsyncGenerator
from enum import StrEnum
from typing import Any, Optional, cast
from boilerplate import get_index, get_timed_logger, batched
from url_obj import url_obj, atp_uri # extra imports for convenience
import re
from atproto import AsyncIdResolver, AsyncDidInMemoryCache, AsyncClient, AtUri
from atproto_client.models.com.atproto.repo.get_record import Response
from atproto_client.models.com.atproto.repo.list_records import Params, Record
log = get_timed_logger("converter")

# afaict these use a single global client so we should be good to loop
resolver = AsyncIdResolver(cache=AsyncDidInMemoryCache())
resolve_handle = resolver.handle.resolve
get_did_doc = resolver.did.resolve

c = AsyncClient()
_get_record = c.com.atproto.repo.get_record
_list_records = c.com.atproto.repo.list_records
base_get = c.request.get

async def get_record(u: atp_uri) -> Response:
    c.update_base_url(await get_pds(u.repo))
    return await _get_record({
        "repo": u.repo,
        "collection": u.collection,
        "rkey": u.rkey
    })


async def get_handle(did: str):
    if doc := await get_did_doc(did):
        return doc.get_handle()

async def get_pds(identifier: str):
    if did := await get_did(identifier):
        if doc := await get_did_doc(did):
            return doc.get_pds_endpoint()
        else:
            log.error(f"could not get pds for {did}")

handle_pattern = re.compile(r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?")

async def get_did(author: str | None):
    if not author:
        log.warning('received empty did')
        return None

    if author.startswith("did:"):
        return author

    if author.startswith("@"):
        author = author[1:]

    if not handle_pattern.match(author):
        log.error(f"Error: invalid handle '{author}'")
        return None

    did = await resolve_handle(author)
    if not did:
        log.error(f"Error retrieving DID '{did}'")
        return None

    return did

async def list_records(u: atp_uri, limit: Optional[int] = 100, batch_size: Optional[int] = 100,) -> AsyncGenerator[Record, Any]:
    c.update_base_url(await get_pds(u.repo))
    if not batch_size:
        batch_size = 100
    if limit and limit < batch_size:
        batch_size = limit
    p = Params(
        collection=u.collection,
        repo=u.repo,
        limit=batch_size
    )
    while limit is None or limit > 0:
        #TODO maybe add an eager fetch that immediately fetches the next batch again
        r = await _list_records(p)

        for rec in r.records:
            yield rec

        if limit:
            limit -= len(r.records)
            p.limit = min(batch_size, limit)

        if not r.cursor or (limit and limit <= 0):
            return
        else:
            p.cursor = r.cursor

async def find_record(u: atp_uri, match_dict: dict[str, Any], limit: Optional[int] = 100, batch_size: int = 100) -> Record | None:
    rec_list = list_records(u, limit, batch_size)
    async for rec in rec_list:
        # un-import-able atproto_client.models.dot_dict - not actually dict, but a model that contains a dict and allows dot notation
        rec_value: dict[str, Any] = cast(dict, rec.value)
        if match_dict.keys() <= rec_value.keys(): # dict.keys() can do everything in collections.abc.Set
            if all(rec_value[k] == v for k,v in match_dict.items()):
                await rec_list.aclose()
                return rec

class bsky_lex(StrEnum):
    like = "app.bsky.feed.like"
    profile = "app.bsky.actor.profile"
    list = "app.bsky.graph.list"
    # listitem = "app.bsky.graph.listitem"
    block = "app.bsky.graph.block"
    labeler = "app.bsky.labeler.service"
    repost = "app.bsky.feed.repost"
    starterpack = "app.bsky.graph.starterpack"
    feed = "app.bsky.feed.generator"
    # threadgate = "app.bsky.feed.threadgate"
    listblock = "app.bsky.graph.listblock"
    follow = "app.bsky.graph.follow"
    # postgate = "app.bsky.feed.postgate"
    post = "app.bsky.feed.post"

async def test_list_records():
    return True
