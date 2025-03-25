from atproto_utils import url_obj, atp_uri

hosts = ['internect.info']

async def handler(u: url_obj) -> atp_uri | None:
    if repo := u.path_index(1):
        return atp_uri(repo)
        
