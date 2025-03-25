from atproto_utils import url_obj, atp_uri, find_record, log

hosts = ['tangled.sh']

async def handler(u: url_obj) -> atp_uri | None:
    if repo := u.path_index(0):
        out = atp_uri(repo, "sh.tangled.repo")
        if tangled_repo := u.path_index(1):
            log.debug(f"searching for {tangled_repo}")
            if rec := await find_record(out, {'name': tangled_repo}):
                return atp_uri.from_str(rec.uri)
            else:
                log.error(f"could not find repo named {tangled_repo} in {out}")
        else:
            return out
    return None
