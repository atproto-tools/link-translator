from atproto_utils import get_index, get_did, url_obj, atp_uri

hosts = ['skylights.my']

async def handler(u: url_obj) -> atp_uri | None:
    if handle := u.path_index(1):
        return atp_uri(handle, "my.skylights.rel")
