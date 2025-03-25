from atproto_utils import url_obj, atp_uri, bsky_lex, log

hosts = ['skychat.social']

params = {
    "thread": bsky_lex.post,
    "likes": bsky_lex.like,
    "follows": bsky_lex.follow
}


async def handler(u: url_obj) -> atp_uri | None:
    match u.split_path(u.fragment):
        case [prefix, repo, *rest]:
            out = atp_uri(repo)
            if collection := params.get(prefix) or bsky_lex.__members__.get(prefix):
                out.collection = collection
            else:
                log.error(f"skychat handler: unknown prefix: {prefix}")
            if len(rest) == 1:
                out.rkey = rest[0]
            else:
                log.error(f"skychat handler: extra elements in path suffix: {rest}")
            return out
