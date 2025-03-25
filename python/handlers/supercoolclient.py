from atproto_utils import url_obj, atp_uri, bsky_lex

hosts = ['supercoolclient.pages.dev']

async def handler(u: url_obj) -> atp_uri | None:
    if repo := u.path_index(0):
        out = atp_uri(repo)
        match u.path[1:]:
            case ["post", rkey]:
                out.collection, out.rkey = bsky_lex.post, rkey
        return out
        
