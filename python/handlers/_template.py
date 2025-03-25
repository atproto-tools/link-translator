from atproto_utils import log, url_obj, atp_uri

# list of hostnames that potentially match this handler
hosts = []

async def handler(u: url_obj) -> atp_uri | None:
    if did := u.path_index(1):
        log.debug(f'handler got {did} from {u.path[1]}')
        return atp_uri(did)
