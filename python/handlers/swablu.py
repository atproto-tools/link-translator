from atproto_utils import url_obj, atp_uri

hosts = ['swablu.pages.dev']

async def handler(u: url_obj) -> atp_uri | None:
    path = u.split_path(u.fragment)
    match path:
        case ["list" | "post", uri]:
            return atp_uri.from_str(uri)
        case ["profile", did]:
            return atp_uri(did)
    return None
