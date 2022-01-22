import unittest
import sys
sys.path.append("../fetch_import")
sys.path.append("../example")
class TestImportAllAttrs(unittest.TestCase):

    def test_path(self):
        self.assertIn("../example",sys.path)
        self.assertIn("../fetch_import",sys.path)
if __name__ == '__main__':
    unittest.main()
