from atproto_utils import bsky_lex, url_obj, atp_uri

hosts = ['blue.mackuba.eu']

async def handler(u: url_obj) -> atp_uri | None:
    if (repo := u.find_query_param("author")) and (rkey := u.find_query_param("post")):
        return atp_uri(repo, bsky_lex.post, rkey)
