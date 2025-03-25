from atproto_utils import get_did, list_records, url_obj, atp_uri, log, get_index
hosts = ['whtwnd.com']

async def handler(u: url_obj) -> atp_uri | None:
    match u:
        case url_obj(path = [handle, entries_or_rkey, *rest]):
            if did := await get_did(handle):
                out = atp_uri(did, "com.whtwnd.blog.entry")
                if entries_or_rkey == "entries":
                    if rkey := u.find_query_param("rkey"):
                        out.rkey = rkey
                    elif title := get_index(rest, 0):
                        checked = 0
                        recs = list_records(out, 200)
                        log.debug(f"searching for {title}")
                        async for rec in recs:
                            checked += 1
                            log.debug(f"got post: {rec.value['title']}")
                            if rec.value['title'] == title:
                                log.debug(f"found after searching {checked} recs")
                                out = atp_uri.from_str(rec.uri)
                                await recs.aclose() # TODO is this call necessary? not sure
                                break
                else:
                    out.rkey = entries_or_rkey
                return out
