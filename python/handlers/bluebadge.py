from atproto_utils import url_obj, atp_uri

hosts = ['badge.blue']

async def handler(u: url_obj) -> atp_uri | None:
    if uri := u.find_query_param("uri"):
        return atp_uri.from_str(uri)
