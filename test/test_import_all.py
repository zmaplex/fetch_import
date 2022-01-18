from pprint import pprint
import unittest

from example.sets import *
from fetch_import import im_fetch

_fetch_module = {}

url = "https://cdn.jsdelivr.net/gh/zmaplex/fetch_import@main/example/sets.py"


class TestImportAllAttrs(unittest.TestCase):

    @im_fetch(url, _globals=_fetch_module, attrs=["*"])
    def test_import_all_attrs(self):
        standard_import_attr = {k: v for k, v in globals().items() if not k.startswith("_")}
        fetch_import_attr = {k: v for k, v in _fetch_module.items() if not k.startswith("_")}
        res = {" standard_import": standard_import_attr,
               "fetch_import": fetch_import_attr}
        # pprint(res)
        pprint(standard_import_attr)
        pprint(fetch_import_attr)

        for attr_name in fetch_import_attr:
            self.assertIn(attr_name, standard_import_attr)


if __name__ == '__main__':
    unittest.main()
