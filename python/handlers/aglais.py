from atproto_utils import bsky_lex, get_index, get_did, url_obj, atp_uri

# source: routes that include the substring '/:did' in https://github.com/mary-ext/aglais/blob/trunk/src/routes.ts
# list of hostnames that potentially match this handler

hosts: list[str] = ['aglais.pages.dev']

async def handler(u: url_obj) -> atp_uri | None:
    if did := await get_did(u.path[0]):
        out = atp_uri(did)
        match get_index(u.path, 1):
            case "curation-lists" | "moderation-lists" | "lists":
                out.collection = bsky_lex.list
                if rkey := get_index(u.path, 2):
                        out.rkey = rkey
            case "following":
                out.collection = bsky_lex.follow
            case "feeds":
                out.collection = bsky_lex.feed
                if rkey := get_index(u.path, 2):
                    out.rkey = rkey
            case "likes":
                out.collection = bsky_lex.like
            case rkey if isinstance(rkey, str):
                out.collection, out.rkey = bsky_lex.post, rkey
            case None:
                out.collection, out.rkey = bsky_lex.profile, "self"
        return out
