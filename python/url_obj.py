# TODO consider switching to a different parsing lib for better validation https://sethmlarson.dev/why-urls-are-hard-path-params-urlparse
from collections.abc import Mapping
from typing import Optional
from urllib.parse import urlparse, parse_qsl, unquote, urlunparse
from atproto_client.models.string_formats import AtIdentifier, Nsid, RecordKey
from boilerplate import get_timed_logger
log = get_timed_logger("url_obj", "debug")

class url_obj:
    def __init__(self, url: str):
        parsed = urlparse(url)
        self.og_parsed = parsed
        self.og = url
        
        self.scheme = parsed.scheme
        self.netloc = parsed.netloc
        self.path = url_obj.split_path(parsed.path)
        self.params = parsed.params # the red headed step child of urlparse :(
        self.query = url_obj.parse_query(parsed.query)
        self.fragment = parsed.fragment
        
    @staticmethod
    def split_path(path_str: str) -> list[str]:
        return [unquote(i) for i in path_str.split("/") if i]

    @staticmethod
    def parse_query(query_str: str) -> list[tuple[str, str]]:
        return [(unquote(k), unquote(v)) for k, v in parse_qsl(query_str)]

    def path_index(self, index: int, default: Optional[str] = None):
        try:
            return self.path[index]
        except IndexError:
            return default

    def find_query_param(self, param: str, query_string: str = '') -> str | None:
        """finds the value of first matching param in the url query"""
        source = url_obj.parse_query(query_string) if query_string else self.query
        return next((p[1] for p in source if p[0] == param), None)

class atp_uri(Mapping):
    """object that stores components of an at URI. original segments are acessible by values, munged versions acessible by dot notation"""
    # @validate_call(config={"strict": True})
    def __init__(
        self,
        # repo: AtIdentifier,
        # collection: Nsid = "",
        # rkey: RecordKey = "",
        repo: str,
        collection: Optional[str] = "",
        rkey: Optional[str] = "",
        query: Optional[str] = "",
        fragment: Optional[str] = "",
    ):
        if not repo:
            raise ValueError(f'no valid repo in atp_uri constructor! args: {locals()}')
        self.repo: AtIdentifier = repo.removeprefix("@") # "@ prefix not valid but reserved for future use"
        self.collection: Nsid = collection or ""
        self.rkey: RecordKey = rkey or ""
        self.query = atp_uri.parse_query(query or "")
        self.fragment = fragment or ""

    parts = ("repo", "collection", "rkey", "query", "fragment")

    @classmethod
    def from_str(cls, url: str):
        parsed = urlparse(url)
        repo = parsed.netloc
        path = atp_uri.split_path(parsed.path)
        collection = path[0]
        if len(path) == 2:
            rkey = path[1]
        elif len(path) > 2:
            raise ValueError(f'atp_uri.from_str: invalid atproto url path: {url}')
        else:
            rkey = ""
        query = parsed.query
        fragment = parsed.fragment
        return cls(repo, collection, rkey, query, fragment)

    @staticmethod
    def split_path(path_str: str) -> list[str]:
        return [unquote(i) for i in path_str.split("/") if i]

    @staticmethod
    def parse_query(query_str: str) -> list[tuple[str, str]]:
        return [(k, unquote(v)) for k, v in parse_qsl(query_str)]

    def find_query_param(self, param: str, query_string: str = '') -> str | None:
        """finds the value of first matching param in the url query"""
        source = url_obj.parse_query(query_string) if query_string else self.query
        return next((p[1] for p in source if p[0] == param), None)

    def has_record(self):
        return bool(self.collection) and bool(self.rkey)

    def __iter__(self):
        yield from self._get_parts()

    def __getitem__(self, key: str):
        if key in atp_uri.parts:
            return getattr(self, key)
        else:
            raise KeyError(f"{key} is not a valid part of an atp_uri")
        
    def __len__(self):
        return len(self._get_parts())

    def _get_parts(self):
        return {part: part_val for part in atp_uri.parts if (part_val := getattr(self, part, None))}
        # return tuple(part_val for part in atp_uri.parts if (part_val := getattr(self, part)))

    def __eq__(self, value) -> bool:
        if isinstance(value, atp_uri):
            return self._get_parts() == value._get_parts()
        else:
            return False

    def __str__(self):
        cs = getattr(self, "collection", "")
        rs = getattr(self, "rkey", "")
        ps = cs + "/" + rs if rs else cs
        ql = getattr(self, "query", [])
        qs = "&".join("=".join((i[0], i[1])) for i in ql) if self.query else ""
        return urlunparse(("at", self.repo, ps, "", qs, self.fragment))
