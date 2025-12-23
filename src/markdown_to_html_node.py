
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType 
from parentnode import ParentNode
from leaftnode import LeafNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType

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

def get_node_tag(block_type, block):
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


 
    
        

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    children = []
    for block in md_blocks:
     

        # trim excess whitespace
        trimmed_block_lines = [line.lstrip(" ") for line in block.split("\n")]
        trimmed_block = "\n".join(trimmed_block_lines)

        block_type = block_to_block_type(trimmed_block)
        node_tag = get_node_tag(block_type, trimmed_block)
 

        match block_type:
            case BlockType.CODE:
                clean_block = trimmed_block.lstrip("```\n").rstrip("```")
                block_node = ParentNode("pre", [text_node_to_html_node(TextNode(clean_block, TextType.CODE) )])
                
            case BlockType.UNORDERED_LIST: 
                clean_block = trimmed_block.replace("\n", "")
                list_items = list(filter(lambda x: x != "", clean_block.split("- ")))
                list_nodes = []
                for li in list_items:  
                    list_nodes.append(ParentNode("li", text_to_children(li))) 
                  

                block_node = ParentNode("ul", list_nodes)
                
            case BlockType.ORDERED_LIST: 
                list_items = trimmed_block.split("\n")
                clean_list_items = list(map(lambda x: x.split(". ")[1], list_items)) 
                list_nodes = []
                for li in clean_list_items: 
                    list_nodes.append(ParentNode("li", text_to_children(li))) 

                block_node = ParentNode("ol", list_nodes) 

            case BlockType.HEADING: 
                clean_block = trimmed_block.split("# ")[1]
                # debug_print(clean_block, "clean_block")
                block_node = LeafNode(node_tag, clean_block)

            case BlockType.QUOTE:
                clean_block = trimmed_block.replace(">", "").lstrip()
                block_node = ParentNode(node_tag, text_to_children(clean_block))

            case _:
                clean_block = trimmed_block.replace("\n", " ")
                block_node = ParentNode(node_tag, text_to_children(clean_block))
    
        children.append(block_node) 

    result = ParentNode("div",  children)  
    # debug_print(result.to_html(), "result")
    return result