from textnode import TextNode, TextType
from htmlnode import HTMLNode


def text_node_to_html_node(text_node):
    if text_node.text_type.value not in TextType:
        raise Exception("Should be a textType")