from atproto_utils import get_index, get_did, url_obj, atp_uri

# list of hostnames that potentially match this handler
hosts = ['atproto-browser.vercel.app']

async def handler(u: url_obj) -> atp_uri | None:
    path = u.path
    if handle := await get_did(get_index(path, 1)):
        out = atp_uri(handle, *path[2:])
        return out
