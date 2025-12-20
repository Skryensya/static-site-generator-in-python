
from src.markdown_to_blocks import markdown_to_blocks
from src.block_to_block_type import block_to_block_type, BlockType 
from src.parentnode import ParentNode
from src.text_to_textnodes import text_to_textnodes
from src.text_node_to_html_node import text_node_to_html_node
from src.textnode import TextNode, TextType

def debug_print(smothing, label):
    print(f"\n-------({label})-----------")
    print(f"{smothing}\n") 


def obtener_heading(texto):
    if not texto:
        return None

    cantidad = len(texto) - len(texto.lstrip("#"))

    if 1 <= cantidad <= 6 and texto[cantidad:cantidad + 1] == " ":
        return cantidad

    return None

def get_node_tag(block, block_type):
    match block_type:
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
            node_tag = "ul" 
        case BlockType.ORDERED_LIST:
            node_tag = "ol" 
    return node_tag

def text_to_children(text): 
    text_nodes = text_to_textnodes(text)
    nodes = []
    for t_node in text_nodes: 
        leaf_node = text_node_to_html_node(t_node)  
        nodes.append(leaf_node)

    return nodes


def clean_text(text, block_type):
    trim_lines = [line.lstrip(" ") for line in text.split("\n")]
    joined_text = "\n".join(trim_lines)
    if block_type == BlockType.CODE: 
        return joined_text.lstrip("```\n").rstrip("```")
    elif  block_type == BlockType.QUOTE: 
        return joined_text.replace("> ", "")
    else:
        return joined_text.replace("\n", " ")
        

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    children = []
    for block in md_blocks:
        block_type = block_to_block_type(block)
        node_tag = get_node_tag(block, block_type)
        if (block_type == BlockType.CODE):
            cleaned_text = clean_text(block, BlockType.CODE)  
            block_node = ParentNode("pre", [text_node_to_html_node(TextNode(cleaned_text, TextType.CODE) )])
        else:
            cleaned_text = clean_text(block, block_type) 
            block_node = ParentNode(node_tag, text_to_children(cleaned_text))

      
        children.append(block_node) 

    result = ParentNode("div",  children)  
    # debug_print(result.to_html(), "result")
    return result