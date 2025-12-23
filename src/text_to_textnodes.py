from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text): 
    base_node = [TextNode(text, TextType.TEXT)]
    with_bold = split_nodes_delimiter(base_node, "**", TextType.BOLD)
    with_italic = split_nodes_delimiter(with_bold, "_", TextType.ITALIC)
    with_code = split_nodes_delimiter(with_italic, "`", TextType.CODE)
    with_link = split_nodes_link(with_code)
    with_images = split_nodes_image(with_link)
    
    return with_images
