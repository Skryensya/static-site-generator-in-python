from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props) 
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag cannot be None for ParentNode")
        if self.children == None:
            raise ValueError("Children cannot be None for ParentNode")
        
        children_html = ""
        for child in self.children:
            if not hasattr(child, "to_html"):
                raise ValueError("All children must have a to_html method")
            children_html += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>" 