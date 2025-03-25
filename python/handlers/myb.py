from atproto_utils import bsky_lex, url_obj, atp_uri

hosts = ['myb.zeu.dev']

async def handler(u: url_obj) -> atp_uri | None:
    match u.path:
        case ["p", repo, "stats"]:
            return atp_uri(repo)
        case ["p", repo, *rest]:
            out = atp_uri(repo)
            if len(rest) == 1:
                out.collection, out.rkey = bsky_lex.post, rest[0]
            return out
    return None

#TODO what is going ON in the third test case https://myb.zeu.dev/?iss=https%3A%2F%2Fbsky.social&state=irWF0wPDsfUb-eHIVBw0qg&code=cod-f41b1cbf3aa4623e72fea7ee9381dc5c8f26571b2f76c51b1de16ebe56cad447
