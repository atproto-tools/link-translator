from atproto_utils import get_index, url_obj, atp_uri

# not sure where the code lives that handles fragments. ctrl-f only gave this https://github.com/shinolabs/PinkSea/blob/master/PinkSea.Frontend/src/api/tegaki/tegaki.js#L1436
hosts = ['pinksea.art']
pinksea = "com.shinolabs.pinksea.oekaki"

async def handler(u: url_obj) -> atp_uri | None:
    match u:
        case url_obj(path=[repo, _, *rest], fragment=frag):
            if frag:
                frag_repo, _, rkey = frag.rpartition("-")
                return atp_uri(frag_repo, pinksea, rkey)
            elif repo:
                return atp_uri(repo, pinksea, get_index(rest, 0))
    return None
