import unittest 
from src.block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_headings(self):
        results = [
            block_to_block_type("###### Heading #6"),
            block_to_block_type("##### Heading #5"),
            block_to_block_type("#### Heading #4"),
            block_to_block_type("### Heading #3"),
            block_to_block_type("## Heading #2"),
            block_to_block_type("# Heading #1"), 
        ] 
        self.assertListEqual([
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
        ], results)

    def test_block_to_block_type_quote(self):
        block = """>Hola
>Mundo"""
        result = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, result)

    def test_block_to_block_type_code(self):
        block = "```<div>Hola Mundo</div>```"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, result)

    def test_block_to_block_type_unordered_list(self):
        block = """- Hola
- Mundo"""
        result = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, result)

    def test_block_to_block_type_ordered_list(self):
        block = """1. Hola
2. Mundo"""
        result = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, result)
        

    def test_block_to_block_type_parragraph(self):
        block = "Parrafo normal"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, result)


if __name__ == "__main__":
    unittest.main()