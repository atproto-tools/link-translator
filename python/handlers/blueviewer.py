from atproto_utils import url_obj, atp_uri, bsky_lex

hosts = ['blueviewer.pages.dev']

async def handler(u: url_obj) -> atp_uri | None:
    if (repo := u.find_query_param("actor")) and (rkey := u.find_query_param("rkey")):
        return atp_uri(repo, bsky_lex.post, rkey)
    return None
