from atproto_utils import url_obj, atp_uri

hosts = ['pastesphere.link']

async def handler(u: url_obj) -> atp_uri | None:
    if handle := u.path_index(1):
        out = atp_uri(handle, "link.pastesphere.snippet")
        if rkey := u.path_index(3):
            out.rkey = rkey
        return out
