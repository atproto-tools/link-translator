import re
from atproto_utils import  url_obj, atp_uri, base_get

hosts = ['recipe.exchange']

async def handler(u: url_obj) -> atp_uri | None:
    match u.path:
        case ["recipes", _]:
            # look man i dont like it either
            r = await base_get(u.og)
            if link := re.search(r"\"(at://.*?)\"", str(r.content)):
                return atp_uri.from_str(link[1])
        case ["profiles", repo]:
            return atp_uri(repo, "exchange.recipe.recipe")
