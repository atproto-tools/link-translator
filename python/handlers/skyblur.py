from atproto_utils import url_obj, atp_uri

hosts = ['skyblur.uk']

async def handler(u: url_obj) -> atp_uri | None:
    if repo := u.path_index(1):
        out = atp_uri(repo, "uk.skyblur.post")
        if rkey := u.path_index(2):
            out.rkey = rkey
        return out
