# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.common.abstracts import Package

# Originally proposed by David Maciejak.

class PS1(Package):
    """PowerShell analysis package."""
    PATHS = [
        ("SystemRoot", "system32", "WindowsPowerShell", "v*.0", "powershell.exe"),
    ]

    def start(self, path):
        powershell = self.get_path_glob("PowerShell")
        args = "-NoProfile -ExecutionPolicy unrestricted -File \"{0}\"".format(path)
        return self.execute(powershell, args, path)
