from atproto_utils import get_did, url_obj, atp_uri
from boilerplate import get_index

# list of hostnames that potentially match this handler
hosts = ["atproto.camp"]

async def handler(u: url_obj) -> atp_uri | None:
    if did := await get_did(get_index(u.path, 0)):
        out = atp_uri(did, "blue.badge.collection")
        if rkey := get_index(u.path, 1):
            out.rkey = rkey
        return out
