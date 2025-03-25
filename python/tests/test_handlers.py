from collections.abc import Awaitable, Callable
import json
import pytest
import inspect
from url_obj import atp_uri, url_obj
import atproto_utils
from handlers._test_data import test_handle, test_did
from handlers_lookup_gen import modules

test_case_dir = "../handler_test_cases"

async def handler_to_str(handler: Callable[[url_obj], Awaitable[atp_uri | None]], val: str):
    result = await handler(url_obj(val))
    if result:
        did = await get_did(result.repo)
        assert did
        result.repo = did
    assert isinstance(result, atp_uri) or result is None, f"handler must return atp_uri object, instead returned {result}"
    return str(result)

async def get_did(handle: str):
    if handle == test_handle:
        return test_did
    else:
        return await atproto_utils.get_did(handle)

async def get_handle(did: str):
    if did == test_did:
        return test_handle
    else:
        return await atproto_utils.get_handle(did)

def get_test_cases():
    """Find all modules with handler functions and test cases."""
    test_params = []
    for module in modules:
        module_name = module.__name__.split(".")[-1]
        setattr(module, "get_did", get_did)
        setattr(module, "get_handle", get_handle)
        if inspect.iscoroutinefunction(module.handler): # trust no one, not even yourself
            test_cases = json.load(open((f"{test_case_dir}/{module_name}.json")))
            for i, test_case in enumerate(test_cases):
                match test_case:
                    case [str(), str()]:
                        test_params.append((module, test_case, i))
                    case _:
                        raise ValueError(f"unexpected shape of test case {i} in {module_name}: {test_case}")
        else:
            raise ValueError(f"module {module_name} handler is not an async function")
    return test_params

@pytest.mark.parametrize("module,case,case_index", get_test_cases())
async def test_handlers(module, case, case_index, monkeypatch):
    # monkeypatch.setenv("ATPROTO_LOG_LEVEL", "debug") # setenv didn't work either. idk
    # idk why this didn't work "properly" with monkeypatch but whatever, we just brute force it above ^
    # tried patching it in the main module where get_did is defined, and the individual module where it's imported
    # monkeypatch.setattr(module, "get_did", get_did)
    # monkeypatch.setattr(module, "get_handle", get_handle)
    module_name = module.__name__.split(".")[-1]
    input_url, expected_url = case
    atproto_utils.log.debug(f"testing {module_name} handler {case_index} url:\n{input_url}")
    result = await handler_to_str(module.handler, input_url)
    atproto_utils.log.debug(f"pdsls url: https://pdsls.dev/{result}")
    assert result == expected_url, (
        f"\nCase:     {module_name} {case_index}\n"
        f"Input:    {input_url}\n"
        f"Expected: {expected_url}\n"
        f"Actual:   {result}"
    )

def test_host_uniqueness():
    handlers_key = {}
    for module in modules:
        for host in module.hosts:
            assert host not in handlers_key
            handlers_key[host] = module.handler
