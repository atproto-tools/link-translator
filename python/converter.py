from handlers_lookup import handlers_lookup
from typing import Any, Optional
from atproto_utils import atp_uri, url_obj, get_record, get_did, log

async def convert(url: str, check_did: Optional[bool] = True) -> atp_uri | None:
    u_obj = url_obj(url)
    netloc = u_obj.netloc
    log.debug(f"invoking handler for {netloc}")
    out = await handlers_lookup[netloc](u_obj)
    if not out:
        log.error(f"no result from {netloc}")
        return None
    if check_did:
        if did := await get_did(out.repo):
            out.repo =  did
        else:
            log.error(f"did not found for {out.repo}")
    return out

async def convert_and_fetch(url_str: str) -> dict[str, Any]:
    uri = await convert(url_str)
    assert uri
    r = await get_record(uri) #type: ignore
    return r.model_dump()
