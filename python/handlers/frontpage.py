from atproto_utils import url_obj, atp_uri

hosts = ['frontpage.fyi']

async def handler(u: url_obj) -> atp_uri | None:
    match u.path:
        case ["post", repo, rkey]:
            return atp_uri(repo, "fyi.unravel.frontpage.post", rkey)
        case ["post", _, _, repo, rkey]:
            return atp_uri(repo, "fyi.unravel.frontpage.comment", rkey)
        case ["profile", repo]:
            return atp_uri(repo)
    return None

# TODO frontpage should add in URLs for posts/comments like reddit has. for now it has profile URLs but not collection-specific ones.
