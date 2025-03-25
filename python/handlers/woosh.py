from atproto_utils import get_index, get_did, url_obj, atp_uri

hosts = ['woosh.link']

async def handler(u: url_obj) -> atp_uri | None:
    if did := await get_did(get_index(u.path, 0)):
        return atp_uri(did)
