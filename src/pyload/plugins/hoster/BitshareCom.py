# -*- coding: utf-8 -*-

from pyload.plugins.internal.deadhoster import DeadHoster


class BitshareCom(DeadHoster):
    __name__ = "BitshareCom"
    __type__ = "hoster"
    __version__ = "0.62"
    __status__ = "testing"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?bitshare\.com/(files/)?(?(1)|\?f=)(?P<ID>\w+)(?(1)/(?P<NAME>.+?)\.html)"
    __config__ = [("enabled", "bool", "Activated", True)]

    __description__ = """Bitshare.com hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [("Paul King", None), ("fragonib", "fragonib[AT]yahoo[DOT]es")]
