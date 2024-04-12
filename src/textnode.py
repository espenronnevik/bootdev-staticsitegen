class TextNode(object):

    def __init__(self, text, text_type, url = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object, /) -> bool:
        return (self.text == value.text and
            self.text_type == value.text_type and
            self.url == value.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_parts = []

    if len(old_nodes) == 0:
        return []

    try:
        node = old_nodes[0]
        node_text_type = node.text_type
        node_parts = node.text.split(delimiter)
    except:
        raise TypeError(f"{old_nodes[0]}is not a TextNode")

    parts_length = len(node_parts)
    if parts_length % 2 == 0:
        raise SyntaxError("Invalid markdown syntax")

    if node_text_type == "text":
        for i in range(parts_length):
            if node_parts[i] == "":
                continue
            if i % 2 == 0:
                new_node = TextNode(node_parts[i], "text")
            else:
                new_node = TextNode(node_parts[i], text_type)
            new_parts.append(new_node)
    else:
        new_parts.append(node)

    new_parts.extend(split_nodes_delimiter(old_nodes[1:], delimiter, text_type))
    return new_parts

def extract_markdown_images(text):
    return []

def extract_markdown_links(text):
    return []
