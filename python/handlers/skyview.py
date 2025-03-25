from atproto_utils import url_obj, atp_uri
from handlers.bluesky import handler as bsky_handler

hosts = ['skyview.social']

async def handler(u: url_obj) -> atp_uri | None:
    if link := u.find_query_param("url"):
        return await bsky_handler(url_obj(link))
    return None
