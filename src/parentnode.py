from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
        self.check_values()

    def check_values(self):
        if self.tag is None or self.tag == "":
            raise ValueError("ParentNode requires a tag")
        if self.children is None or len(self.children) == 0:
           raise ValueError("ParentNode requires children")

    def to_html(self):
        self.check_values()
        cs = "".join(map(lambda node: node.to_html(), self.children))
        if self.props is None:
            return f"<{self.tag}>{cs}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{cs}</{self.tag}>"
