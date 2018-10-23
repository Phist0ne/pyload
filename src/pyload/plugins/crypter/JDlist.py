# -*- coding: utf-8 -*-

from pyload.plugins.internal.crypter import Crypter


class JDlist(Crypter):
    __name__ = "JDlist"
    __type__ = "crypter"
    __version__ = "0.05"
    __status__ = "testing"

    __pyload_version__ = "0.5"

    __pattern__ = r"jdlist://(?P<LIST>[\w\+^_]+==)"
    __config__ = [
        ("enabled", "bool", "Activated", True),
        ("use_premium", "bool", "Use premium account if available", True),
        (
            "folder_per_package",
            "Default;Yes;No",
            "Create folder for each package",
            "Default",
        ),
    ]

    __description__ = """JDlist decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [("Walter Purcaro", "vuolter@gmail.com")]

    def decrypt(self, pyfile):
        self.links.extend(self.info["pattern"]["LIST"].decode("base64").split(","))
