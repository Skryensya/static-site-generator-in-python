import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("text node #1", TextType.BOLD)
        node2 = TextNode("text node #2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_link_eq(self):
        node = TextNode("boot.dev site", TextType.BOLD, "boot.dev")
        node2 = TextNode("boot.dev site", TextType.BOLD, "boot.dev")
        self.assertEqual(node, node2)



if __name__ == "__main__":
    unittest.main()