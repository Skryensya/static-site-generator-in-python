from markdown_to_blocks import markdown_to_blocks 

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    heading_blocks = list(filter(lambda x: x.startswith("# "), blocks))
    if (len(heading_blocks) == 0):
        raise Exception("Should have at least one heading")
    
    return heading_blocks[0].lstrip("# ")  