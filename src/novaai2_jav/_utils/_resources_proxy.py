from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `novaai2_jav.resources` module.

    This is used so that we can lazily import `novaai2_jav.resources` only when
    needed *and* so that users can just import `novaai2_jav` and reference `novaai2_jav.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("novaai2_jav.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
