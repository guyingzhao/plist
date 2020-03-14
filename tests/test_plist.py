# -*- coding: utf-8 -*-
"""test plist info
"""

import os
import unittest

from plist import PlistInfo


cur_dir = os.path.dirname(os.path.abspath(__file__))


class PlistInfoTest(unittest.TestCase):

    def check_plist(self, p):
        self.assertEqual(p["CFBundleIdentifier"], "com.guying.app.foo")
        self.assertEqual(p["CFBundleName"], "FooApp")
        self.assertEqual(p["CFBundleExecutable"], "FooApp")

    def test_raw_file(self):
        plist_file = os.path.join(cur_dir, "Info.plist")
        p = PlistInfo.from_file(plist_file)
        self.check_plist(p)

        temp_file = "temp.plist"
        p.to_binary_file(temp_file)
        self.assertTrue(os.path.isfile(temp_file))
        self.addCleanup(os.remove, temp_file)
        new_p = PlistInfo.from_file(temp_file)
        self.assertEqual(new_p, p)

    def test_app(self):
        app_path = os.path.join(cur_dir, "FooApp.app")
        p = PlistInfo.from_app(app_path)
        self.check_plist(p)

    def test_ipa(self):
        app_path = os.path.join(cur_dir, "FooApp.ipa")
        p = PlistInfo.from_app(app_path)
        self.check_plist(p)

    def test_xml_plist(self):
        plist_file = os.path.join(cur_dir, "Info.xml")
        p = PlistInfo.from_file(plist_file)
        self.check_plist(p)

        xml_file = "temp.xml"
        p.to_xml_file(xml_file)
        self.assertTrue(os.path.isfile(xml_file))
        self.addCleanup(os.remove, xml_file)
        new_p = PlistInfo.from_file(xml_file)
        self.assertEqual(new_p, p)


if __name__ == "__main__":
    unittest.main(defaultTest="PlistInfoTest.test_xml_plist")
