import math
from src.textnode import TextNode, TextType
from src.extract_markdown_images import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != TextType.TEXT):
            new_nodes.append(node)
        else:
            images_match = extract_markdown_images(node.text)
            if (len(images_match or []) == 0): 
                new_nodes.append(node)
                continue
            current_img = images_match[0] 
    
            first_split = node.text.split(f"![{current_img[0]}]({current_img[1]})", 1)
            prev = first_split[0]
            next = first_split[1]  
            rest_node = TextNode(next, TextType.TEXT) 
            
            next_nodes = []
            if(len(images_match) == 1):
                if (next != ""):
                    next_nodes.append(rest_node)
            else:
                next_nodes = split_nodes_image([rest_node])

 

            new_nodes.extend([
                TextNode(prev, TextType.TEXT),
                TextNode(current_img[0], TextType.IMAGE, current_img[1]), 
            ])
            new_nodes.extend(next_nodes)

            ni = 0
            # filter "" text nodes
            for node  in new_nodes:
                if (node == TextNode("", TextType.TEXT)):
                    new_nodes.pop(ni) 
                ni +=1 
 
    return new_nodes
