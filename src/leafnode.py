from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None) -> None:
        super().__init__(tag, value, None, props)
        self.check_values()

    def check_values(self):
        if self.value is None:
            raise ValueError("LeafNode requires a value")

    def to_html(self):
        self.check_values()
        if self.tag is None:
            return self.value
        elif self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"


def text_node_to_html_node(text_node):
    try:
        if text_node.text_type == "text":
            return LeafNode(text_node.text)
        elif text_node.text_type == "bold":
            return LeafNode(text_node.text, "b")
        elif text_node.text_type == "italic":
            return LeafNode(text_node.text, "i")
        elif text_node.text_type == "code":
            return LeafNode(text_node.text, "code")
        elif text_node.text_type == "link":
            return LeafNode(text_node.text, "a", {"href": text_node.url})
        elif text_node.text_type == "image":
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
        else:
            raise Exception(f"Unsupported text type {text_node.text_type}")
    except:
        raise Exception("text_node_to_html_node() requires a TextNode")
