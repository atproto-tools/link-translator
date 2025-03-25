from atproto_utils import url_obj, atp_uri

hosts = ['plonk.li']

async def handler(u: url_obj) -> atp_uri | None:
    match u.path:
        case ["u", did]:
            return atp_uri(did, "li.plonk.paste")
