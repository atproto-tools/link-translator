from atproto_utils import get_index, url_obj, atp_uri

hosts = ['popsky.social']

async def handler(u: url_obj) -> atp_uri | None:
    if uri := get_index(u.path, 1):
        return atp_uri.from_str(uri)
