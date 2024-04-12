class HTMLNode(object):
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            res = []
            for k, v in self.props.items():
                res.append(f'{k}="{v}"')
            return " ".join(res)

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None) -> None:
        super().__init__(tag, value, None, props)
        self.check_values()

    def check_values(self):
        if self.value is None or self.value == "":
            raise ValueError("LeafNode requires a value")

    def to_html(self):
        self.check_values()
        if self.tag is None:
            return self.value
        elif self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
        self.check_values()

    def check_values(self):
        if self.tag is None or self.tag == "":
            raise ValueError("ParentNode requires a tag")
        if self.children is None or len(self.children) == 0:
           raise ValueError("ParentNode requires children")
