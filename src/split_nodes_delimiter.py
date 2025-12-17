import math
from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = [] 
    for node in old_nodes:
        if (node.text_type != TextType.TEXT):
            new_nodes.append(node)
        else:
            splitted = node.text.split(delimiter)

            for key, value in enumerate(splitted):
                if key % 2 == 0: 
                    new_nodes.append(TextNode(value, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(value, text_type))
        
            
            for key, node in enumerate(new_nodes):
                if (node == TextNode("", TextType.TEXT)):
                    new_nodes.pop(key) 
                 
    return new_nodes
