from enum import Enum

class BlockType(Enum):
   PARAGRAPH = "paragraph"
   HEADING = "heading"
   CODE = "code"
   QUOTE = "quote"
   UNORDERED_LIST = "unordered_list"
   ORDERED_LIST = "ordered_list"

def block_to_block_type(block): 
  lines = block.split("\n")

  if block.startswith("```") and block.endswith("```"):
    return BlockType.CODE
  
  if block.startswith("###### "): 
    return BlockType.HEADING
  if block.startswith("##### "): 
    return BlockType.HEADING
  if block.startswith("#### "): 
    return BlockType.HEADING
  if block.startswith("### "): 
    return BlockType.HEADING
  if block.startswith("## "): 
    return BlockType.HEADING
  if block.startswith("# "): 
    return BlockType.HEADING
  
  if all([x.startswith(">") for x in lines]): 
    return BlockType.QUOTE
  
  if all([x.startswith("- ") for x in lines]): 
    return BlockType.UNORDERED_LIST
  
  if all([x.isdigit() for x in [y.split(". ", 1)[0] for y in lines]]): 
    return BlockType.ORDERED_LIST 

  return BlockType.PARAGRAPH
 