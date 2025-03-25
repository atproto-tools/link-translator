from atproto_utils import bsky_lex, get_index, log, url_obj, atp_uri

hosts = ["bsky.app", "main.bsky.dev", "langit.pages.dev", "tokimekibluesky.vercel.app"]
async def handler(u: url_obj) -> atp_uri | None:
    if u.netloc ==  "langit.pages.dev":
        match u.path:
            case ["u", _, *rpath]:
                u.path = rpath
            case _:
                return None
    did = u.path_index(1)
    if not did:
        return None

    match u.path_index(0):
        case "starter-pack":
            return atp_uri(did, bsky_lex.starterpack, u.path[2])
        case "profile":
            if rkey := get_index(u.path, 3):
                match u.path[2]:
                    case "post":
                        return atp_uri(did, bsky_lex.post, rkey)
                    case "feed":
                        return atp_uri(did, bsky_lex.feed, rkey)
                    case "lists":
                        return atp_uri(did, bsky_lex.list, rkey)
                    case "follows":
                        return atp_uri(did, bsky_lex.follow)
                    case _:
                        log.error(f"uknown suffix {u.path[2]} in {u.og}")
            else:
                return atp_uri(did, bsky_lex.profile, "self")
