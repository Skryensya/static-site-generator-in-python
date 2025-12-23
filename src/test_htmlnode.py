import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", None, None, {"href": "https://boot.dev"}) 
        node2 = HTMLNode("a", None, None, {"href": "https://boot.dev"}) 
        self.assertEqual(node.props_to_html(), node2.props_to_html())
    def test_props_to_html_not_equal(self):
        node = HTMLNode("span", None, None, {"href": "https://boot.dev"}) 
        node2 = HTMLNode("span", None, None, {"href": "https://boot.dev/about"}) 
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())
    def test_eq_html_node(self):
        node = HTMLNode("div", None, None, {"href": "https://boot.dev"})
        node2 = HTMLNode("div", None, None, {"href": "https://boot.dev"})
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()