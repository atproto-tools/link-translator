from atproto_utils import url_obj, atp_uri

hosts = ['cdn.bsky.app', 'video.bsky.app']

async def handler(u: url_obj) -> atp_uri | None:
    match u:
        case url_obj(netloc="cdn.bsky.app"):
            if repo := u.path_index(3):
                return atp_uri(repo, "blobs")
        case url_obj(netloc="video.bsky.app"):
            if repo := u.path_index(1):
                return atp_uri(repo, "blobs")
    return None
