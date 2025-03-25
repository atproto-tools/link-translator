from handlers.aglais import handler as aglais
from handlers.atbrowser import handler as atbrowser
from handlers.atprofile import handler as atprofile
from handlers.atprotocamp import handler as atprotocamp
from handlers.atptools import handler as atptools
from handlers.bluebadge import handler as bluebadge
from handlers.bluesky import handler as bluesky
from handlers.blueviewer import handler as blueviewer
from handlers.bookhive import handler as bookhive
from handlers.bskycdn import handler as bskycdn
from handlers.clearsky import handler as clearsky
from handlers.flushes import handler as flushes
from handlers.frontpage import handler as frontpage
from handlers.internect import handler as internect
from handlers.klearsky import handler as klearsky
from handlers.linkat import handler as linkat
from handlers.myb import handler as myb
from handlers.ouranos import handler as ouranos
from handlers.pastesphere import handler as pastesphere
from handlers.pinboards import handler as pinboards
from handlers.pinksea import handler as pinksea
from handlers.pinksky import handler as pinksky
from handlers.plonk import handler as plonk
from handlers.popsky import handler as popsky
from handlers.recipeexchange import handler as recipeexchange
from handlers.ruthub import handler as ruthub
from handlers.skyblur import handler as skyblur
from handlers.skychat import handler as skychat
from handlers.skylights import handler as skylights
from handlers.skythread import handler as skythread
from handlers.skyview import handler as skyview
from handlers.skywatched import handler as skywatched
from handlers.smokesignal import handler as smokesignal
from handlers.supercoolclient import handler as supercoolclient
from handlers.swablu import handler as swablu
from handlers.tangled import handler as tangled
from handlers.whitewind import handler as whitewind
from handlers.woosh import handler as woosh
from handlers.xrpc import handler as xrpc


handlers_lookup = {
    "aglais.pages.dev": aglais,
    "atproto-browser.vercel.app": atbrowser,
    "atprofile.com": atprofile,
    "atproto.camp": atprotocamp,
    "atp.tools": atptools,
    "badge.blue": bluebadge,
    "bsky.app": bluesky,
    "main.bsky.dev": bluesky,
    "langit.pages.dev": bluesky,
    "tokimekibluesky.vercel.app": bluesky,
    "blueviewer.pages.dev": blueviewer,
    "bookhive.buzz": bookhive,
    "cdn.bsky.app": bskycdn,
    "video.bsky.app": bskycdn,
    "clearsky.app": clearsky,
    "flushes.app": flushes,
    "frontpage.fyi": frontpage,
    "internect.info": internect,
    "klearsky.pages.dev": klearsky,
    "linkat.blue": linkat,
    "myb.zeu.dev": myb,
    "useouranos.app": ouranos,
    "pastesphere.link": pastesphere,
    "pinboards.jeroba.xyz": pinboards,
    "pinksea.art": pinksea,
    "pinksky.app": pinksky,
    "psky.co": pinksky,
    "plonk.li": plonk,
    "popsky.social": popsky,
    "recipe.exchange": recipeexchange,
    "ruthub.com": ruthub,
    "skyblur.uk": skyblur,
    "skychat.social": skychat,
    "skylights.my": skylights,
    "blue.mackuba.eu": skythread,
    "skyview.social": skyview,
    "skywatched.app": skywatched,
    "smokesignal.events": smokesignal,
    "supercoolclient.pages.dev": supercoolclient,
    "swablu.pages.dev": swablu,
    "tangled.sh": tangled,
    "whtwnd.com": whitewind,
    "woosh.link": woosh,
    "public.api.bsky.app": xrpc,
}
