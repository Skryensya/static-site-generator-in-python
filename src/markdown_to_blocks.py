def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n") 
    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = list(filter(lambda x: x != "", blocks))

    return blocks