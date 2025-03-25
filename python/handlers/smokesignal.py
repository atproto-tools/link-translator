from atproto_utils import url_obj, atp_uri

hosts = ['smokesignal.events']

async def handler(u: url_obj) -> atp_uri | None:
    if repo := u.path_index(0):
        out = atp_uri(repo)
        if rkey := u.path_index(1):
            out.collection, out.rkey = "events.smokesignal.calendar.event", rkey
        else:
            out.collection, out.rkey = "events.smokesignal.app.profile", "self"
        return out
