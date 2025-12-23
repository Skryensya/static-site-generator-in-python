import unittest

from textnode import TextNode, TextType
from text_node_to_html_node import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "#url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), f'<a href="#url">This is a link node</a>')

    def test_code(self):
        node = TextNode("code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), f'<code>code</code>')

    def test_img(self):
        node = TextNode("This is an image node", TextType.IMAGE, "#image_src")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), f'<img src="#image_src" alt="This is an image node"></img>')



if __name__ == "__main__":
    unittest.main()