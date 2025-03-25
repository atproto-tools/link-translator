from atproto_utils import url_obj, atp_uri

hosts = ['ruthub.com']

async def handler(u: url_obj) -> atp_uri | None:
    match u.path:
        case ["kb", repo]:
            return atp_uri(repo, "com.ruthub.kanban")
        case ["blog", repo]:
            return atp_uri(repo, "com.ruthub.entry")
        case ["p", repo, rkey]:
            return atp_uri(repo, "com.ruthub.entry", rkey)
        case ["rut", repo]:
            return atp_uri(repo, "com.ruthub.item")
