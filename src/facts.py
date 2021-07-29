"""
HalpyDEMO v0.1

Copyright (c) 2021 The Hull Seals,
All rights reserved.

Licensed under the GNU General Public License
See license.md

"""

import sqlite3

class Facthandler:

    def __init__(self, dbpath: str):
        self._cache = {}
        self.from_database(database=dbpath)

    def from_database(self, database):
        con = sqlite3.connect(database)
        cur = con.cursor()
        for entry in cur.execute("SELECT name, text FROM facts;"):
            self._cache[entry[0]] = entry[1]

    def get_fact(self, name: str):
        if name in self._cache.keys():
            return self._cache[name]
        else:
            return None
