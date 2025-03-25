from atproto_utils import url_obj, atp_uri

hosts = ['pinksky.app', 'psky.co']


async def handler(u: url_obj) -> atp_uri | None:
    match u:
        case url_obj(netloc="psky.co", path=[repo]):
            return atp_uri(repo)
        case url_obj(netloc="pinksky.app") as pinksky:
            match pinksky:
                case url_obj(path=[_, *path]):
                    if uri := u.find_query_param("uri") or u.find_query_param("comments"):
                        return atp_uri.from_str(uri)
                    if path:
                        return atp_uri(*path)
    return None
