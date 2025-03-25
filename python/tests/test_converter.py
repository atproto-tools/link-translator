import pytest
import converter
from atproto_utils import log

@pytest.fixture(autouse=True)
def log_level():
    log.setLevel("DEBUG")

url = "https://klearsky.pages.dev/#/home/starter-pack?uri=at://did:plc:p2cp5gopk7mgjegy6wadk3ep/app.bsky.graph.starterpack/3kztso5fnic24"
atp = "at://did:plc:p2cp5gopk7mgjegy6wadk3ep/app.bsky.graph.starterpack/3kztso5fnic24"
async def test_convert():
    assert str(await converter.convert(url)) == atp
