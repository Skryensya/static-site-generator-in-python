import math
from textnode import TextNode, TextType
from extract_markdown_links import extract_markdown_links

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != TextType.TEXT):
            new_nodes.append(node)
        else:
            links_match = extract_markdown_links(node.text)
            if (len(links_match or []) == 0): 
                new_nodes.append(node)
                continue
            current_link = links_match[0] 
    
            first_split = node.text.split(f"[{current_link[0]}]({current_link[1]})", 1)
            prev = first_split[0]
            next = first_split[1]  
            rest_node = TextNode(next, TextType.TEXT) 
            
            next_nodes = []
            if(len(links_match) == 1):
                if (next != ""):
                    next_nodes.append(rest_node)
            else:
                next_nodes = split_nodes_link([rest_node])

 

            new_nodes.extend([
                TextNode(prev, TextType.TEXT),
                TextNode(current_link[0], TextType.LINK, current_link[1]), 
            ])
            new_nodes.extend(next_nodes)

            ni = 0
            # filter "" text nodes
            for node  in new_nodes:
                if (node == TextNode("", TextType.TEXT)):
                    new_nodes.pop(ni) 
                ni +=1 
 
    return new_nodes
