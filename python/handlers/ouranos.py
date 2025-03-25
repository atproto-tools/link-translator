from atproto_utils import bsky_lex, get_did, url_obj, atp_uri
from boilerplate import get_index

# source https://github.com/pdelfan/ouranos/tree/main/src/app (subfolders are routes)
hosts = ["useouranos.app"]

async def handler(u: url_obj):
    if uri := u.find_query_param("uri"):
        return atp_uri.from_str(uri)
    match get_index(u.path, 1):
        case "user":
            if did := await get_did(u.path[2]):
                if get_index(u.path, 3) == "post":
                    return atp_uri(did, bsky_lex.post, u.path[4])
                return atp_uri(did, bsky_lex.profile, "self")
