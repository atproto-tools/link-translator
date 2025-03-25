from atproto_utils import bsky_lex, get_index, url_obj, atp_uri

hosts = ['clearsky.app']

async def handler(u: url_obj) -> atp_uri | None:
    if did := get_index(u.path, 0):
        out = atp_uri(did)
        match u.path_index(1):
            case "blocking":
                out.collection = bsky_lex.block
            case "history" | None:
                out.collection = bsky_lex.post
            case "packs":
                out.collection = bsky_lex.starterpack
        return out
    return None
