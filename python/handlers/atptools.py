from atproto_utils import url_obj, atp_uri

hosts = ['atp.tools']

async def handler(u: url_obj) -> atp_uri | None:
    match u.path:
        case ["at:", repo, *rest]:
            out = atp_uri(repo)
            if rest:
                out.collection = rest[0]
            return out
    return None
