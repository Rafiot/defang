#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from defang import defanger, refanger
import sys


class TestDefang(unittest.TestCase):

    def test_defanger(self):
        defanger("http://google.fr", sys.stdout)

    def test_refanger(self):
        refanger("hXXp://google[.]fr", sys.stdout)

if __name__ == "__main__":
    unittest.main()
