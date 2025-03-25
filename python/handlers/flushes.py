from atproto_utils import get_did, url_obj, atp_uri
from boilerplate import get_index

hosts = ['flushes.app']

async def handler(u: url_obj) -> atp_uri | None:
    if did := await get_did(get_index(u.path, 1)):
        return atp_uri(did)
