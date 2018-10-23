# -*- coding: utf-8 -*-

from pyload.plugins.internal.deadcrypter import DeadCrypter


class ILoadTo(DeadCrypter):
    __name__ = "ILoadTo"
    __type__ = "crypter"
    __version__ = "0.16"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?iload\.to/go/\d+\-[\w\-.]+/"
    __config__ = [("enabled", "bool", "Activated", True)]

    __description__ = """Iload.to decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [("hzpz", None)]
