from pprint import pprint
import unittest

from example import sets
from fetch_import import im_fetch

_fetch_module = {}

url = "https://fastly.jsdelivr.net/gh/zmaplex/fetch_import@main/example/sets.py"


class TestImportMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self._g = globals()
        super(TestImportMethods, self).__init__(*args, **kwargs)

    @im_fetch(url, _globals=_fetch_module)
    def test_import_module(self):
        res = {" standard_import": {"sets": globals()["sets"]},
               "fetch_import": _fetch_module}
        standard_import_attr = {k: v for k, v in sets.__dict__.items() if not k.startswith("_")}
        fetch_import_attr = {k: v for k, v in _fetch_module["sets"].__dict__.items() if not k.startswith("_")}
        # pprint(res)
        # pprint(standard_import_attr)
        # pprint(fetch_import_attr)

        for attr_name in standard_import_attr:
            self.assertIn(attr_name, fetch_import_attr)


if __name__ == '__main__':
    unittest.main()
