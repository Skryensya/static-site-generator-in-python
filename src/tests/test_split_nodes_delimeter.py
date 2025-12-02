import unittest

from src.textnode import TextNode, TextType
from src.split_nodes_delimiter import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    # def test_code_block_2(self):
    #     node = TextNode("This is text with a `code block` word and another `code block` lol", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    #     self.assertEqual(new_nodes, [
    #         TextNode("This is text with a ", TextType.TEXT),
    #         TextNode("code block", TextType.CODE),
    #         TextNode(" word and another ", TextType.TEXT),
    #         TextNode("code block", TextType.CODE),
    #         TextNode(" lol", TextType.TEXT),
    #     ])
    # def test_code_block_3(self):
    #     node = TextNode("`code block` word and another `code block` `code block`", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    #     self.assertEqual(new_nodes, [
    #         TextNode("This is text with a ", TextType.TEXT),
    #         TextNode("code block", TextType.CODE),
    #         TextNode(" word", TextType.TEXT),
    #     ])


if __name__ == "__main__":
    unittest.main()