class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html in the child class not yet implemented")

    def props_to_html(self):
        props_str = ""
        if(self.props):
            for prop in self.props:
                props_str += f" {prop}={self.props[prop]}"
            return props_str

        return props_str

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag, self.value, self.children, self.props})"


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
            super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf requires a value")

        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
            super().__init__(tag, None, children, props)

    def to_html(self):
        if self.children is None:
            raise ValueError("All parent requires a child")

        if self.tag is None:
            raise ValueError("Tag is needed for parent Node")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

