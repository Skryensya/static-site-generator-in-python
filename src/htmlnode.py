class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None or len(self.props) == 0:
            return ""
        acc_props = []
        for k, v in list(self.props.items()):
            acc_props.append(f' {k}="{v}"')
        return "".join(acc_props)
    
    def __repr__(self):
        if self.tag == None:
            return self.value
        if self.children:
            return f"<{self.tag}{self.props_to_html()}>{self.children}</{self.tag}>"
        else: 
            return f"<{self.tag}{self.props_to_html()}></{self.tag}>"

    def __eq__(self, value):
        return self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props