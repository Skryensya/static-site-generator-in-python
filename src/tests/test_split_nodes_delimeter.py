import unittest

from src.textnode import TextNode, TextType
from src.split_nodes_delimiter import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("A `B` C", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("A ", TextType.TEXT),
            TextNode("B", TextType.CODE),
            TextNode(" C", TextType.TEXT),
        ])

    def test_code_block_2(self):
        node = TextNode("A `B` C `D` E", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("A ", TextType.TEXT),
            TextNode("B", TextType.CODE),
            TextNode(" C ", TextType.TEXT),
            TextNode("D", TextType.CODE),
            TextNode(" E", TextType.TEXT),
        ])
        
    def test_code_block_3(self):
        node = TextNode("`A` B `C` `D`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("A", TextType.CODE),
            TextNode(" B ", TextType.TEXT),
            TextNode("C", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("D", TextType.CODE)
        ])

    def test_italic(self):
        node = TextNode("**A** B **C** **D**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("A", TextType.BOLD),
            TextNode(" B ", TextType.TEXT),
            TextNode("C", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("D", TextType.BOLD)
        ])

if __name__ == "__main__":
    unittest.main()