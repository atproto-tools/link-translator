from atproto_utils import url_obj, atp_uri

hosts = ['bookhive.buzz']

async def handler(u: url_obj) -> atp_uri | None:
    match u.path:
        case ["profile", repo]:
            return atp_uri(repo, "buzz.bookhive.book")
    return None
