#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from defang import defanger, refanger, defang, refang
import sys


class TestDefang(unittest.TestCase):

    def test_defanger(self):
        defanger("http://google.fr", sys.stdout)

    def test_defang(self):
        self.assertEqual(defang("http://google.fr"), "hXXp://google[.]fr")

    def test_refang(self):
        self.assertEqual(refang("hXXp://google[.]fr"), "http://google.fr")
        self.assertEqual(refang("hxxp://google[.]fr"), "http://google.fr")
        self.assertEqual(refang("fXp://google[.]fr"), "ftp://google.fr")
        self.assertEqual(refang("fxp://google[.]fr"), "ftp://google.fr")
        self.assertEqual(refang("purr://google[.]fr"), "http://google.fr")
        self.assertEqual(refang("meow://google[.]fr"), "http://google.fr")

    def test_refanger(self):
        refanger("hXXp://google[.]fr", sys.stdout)


if __name__ == "__main__":
    unittest.main()
