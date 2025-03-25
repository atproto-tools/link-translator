from urllib.parse import unquote
from atproto_utils import get_did, log, url_obj, atp_uri, bsky_lex
from boilerplate import get_index

# source https://github.com/mimonelu/klearsky/blob/staging/src/router/index.ts
# also https://github.com/mimonelu/klearsky/blob/staging/src/views/MainView.vue#L498 ?
# after a while looking at the code i couldn't determine the routing logic (where are url params processed?)
# however i did find this function which partially covers it https://github.com/mimonelu/klearsky/blob/staging/src/components/labels/HtmlText.vue#L99
# edit: after looking at it again, apparently there's just no central function. just search for it instead https://github.com/search?q=repo%3Amimonelu%2Fklearsky%20state.currentQuery&type=code

hosts = ["klearsky.pages.dev"]


async def handler(u: url_obj) -> atp_uri | None:
    frag = u.fragment.split("?")
    if len(frag) != 2:
        log.error(f"got weird klearsky url, investigate: {u.og}")
        return None
    u.path, u.query = url_obj.split_path(frag[0]), u.parse_query(frag[1])

    if uri := next((v for p in ["uri", "list", "feed"] if (v := u.find_query_param(p))), None):
        return atp_uri.from_str(unquote(uri))
    elif account := u.find_query_param("account"):
        out = atp_uri(account)
        match u.path_index(0):
            case "profile":
                match get_index(u.path, 1):
                    case "following":
                        out.collection = bsky_lex.follow
                    case "list":
                        out.collection = bsky_lex.list
                    case "feed-generators":
                        out.collection = bsky_lex.feed
                    case "feeds":
                        out.collection = bsky_lex.post 
                    case None:
                        pass
                    case _ as suffix:
                        log.error(
                            f"error in klearsky when handling {u.og}:\n"
                            f"unknown suffix: {suffix}"
                        )
                        return None
                return out
    elif handle :=  u.find_query_param("handle"):
        if (account := await get_did(handle)) and (rkey := u.find_query_param("rkey")):
            return atp_uri(account, bsky_lex.post, rkey)
    else:
        return None
