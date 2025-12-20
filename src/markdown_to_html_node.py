
from src.markdown_to_blocks import markdown_to_blocks
from src.block_to_block_type import block_to_block_type, BlockType
from src.htmlnode import HTMLNode
from src.parentnode import ParentNode


def obtener_heading(texto):
    if not texto:
        return None

    cantidad = len(texto) - len(texto.lstrip("#"))

    if 1 <= cantidad <= 6 and texto[cantidad:cantidad + 1] == " ":
        return cantidad

    return None

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
 
    children = None
 

    for block in md_blocks:
        type_of_block = block_to_block_type(block)
        node_tag = None
        match type_of_block:
            case BlockType.PARAGRAPH:
                node_tag = "p"
            case BlockType.CODE:
                node_tag = "code" 
            case BlockType.QUOTE:
                node_tag = "blockquote"
            case BlockType.HEADING:
                heading_lvl = obtener_heading(block) 
                node_tag = f"h{heading_lvl}"
            case BlockType.UNORDERED_LIST:
                pass
            case BlockType.ORDERED_LIST:
                pass

                


     


    return  ParentNode("div",  children)