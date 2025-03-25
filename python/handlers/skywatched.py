from atproto_utils import url_obj, atp_uri

hosts = ['skywatched.app']

async def handler(u: url_obj) -> atp_uri | None:
    match u.path:
        case ["review", uri]:
            return atp_uri.from_str(uri)
        case ["user", repo]:
            return atp_uri(repo, "my.skylights.rel")
    return None
