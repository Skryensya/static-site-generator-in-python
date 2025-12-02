import math
from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != TextType.TEXT):
            new_nodes.extend(node)
        else:
            splitted = node.text.split(delimiter)

            if len(splitted) == 1:
                return TextNode(node.text, TextType.TEXT)
            if len(splitted) % 2 == 0:
                raise Exception("That is not valid markdown Syntax")
            
            instances = math.ceil(len(splitted) / 3)

         
            first_split = node.text.split(delimiter, 1)
            prev = first_split[0]
            second_split = first_split[1].split(delimiter, 1)
            actual_block = second_split[0]
            next_nodes = []
            if(instances == 1):
                next_nodes.append(TextNode(second_split[1], TextType.TEXT))
            else:
                next_nodes = split_nodes_delimiter(second_split[1])

            new_nodes.extend([
                TextNode(prev, TextType.TEXT),
                TextNode(actual_block, TextType.CODE), 
            ])
            next_nodes.extend(next_nodes)
    return new_nodes
