import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
   def test_extract_title(self):
        matches = extract_title("""# Hola mundo

        Ayyy ay ayyy, llevatelo todo, que todo te pertenece
        """ 
        )
        self.assertEqual("Hola mundo", matches)

if __name__ == "__main__":
    unittest.main()