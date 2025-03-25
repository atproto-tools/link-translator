from atproto_utils import url_obj, atp_uri

hosts = ['pinboards.jeroba.xyz']

async def handler(u: url_obj) -> atp_uri | None:
    match u.path:
        case ["profile", repo, "board", rkey]:
            return atp_uri(repo, "xyz.jeroba.tags.tag", rkey)
    return None
