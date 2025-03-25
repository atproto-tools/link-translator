from atproto_utils import url_obj, atp_uri

hosts = ['linkat.blue']

async def handler(u: url_obj) -> atp_uri | None:
    if repo := u.path_index(0):
        out = atp_uri(repo, "blue.linkat.board", "self")
        return out
