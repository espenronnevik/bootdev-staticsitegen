import re


class TextNode(object):

    def __init__(self, text, text_type, url=None) -> None:
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
    new_nodes = []

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
            new_nodes.append(new_node)
    else:
        new_nodes.append(node)

    new_nodes.extend(split_nodes_delimiter(old_nodes[1:], delimiter, text_type))
    return new_nodes


def extract_markdown_images(text):
    re_image = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(re_image, text)


def extract_markdown_links(text):
    re_links = r"\[(.*?)\]\((.*?)\)"
    return re.findall(re_links, text)


def split_nodes_images(old_nodes):
    new_nodes = []

    if len(old_nodes) == 0:
        return []

    try:
        node = old_nodes[0]
        node_text = node.text
        node_text_type = node.text_type
    except:
        raise TypeError(f"{old_nodes[0]}is not a TextNode")

    if node_text_type == "text":
        worktext = node_text
        extracted = extract_markdown_images(node_text)
        if len(extracted) > 0:
            for image in extracted:
                md = f"![{image[0]}]({image[1]})"
                parts = worktext.partition(md)
                if parts[0] != "":
                    new_nodes.append(TextNode(parts[0], "text"))
                new_nodes.append(TextNode(image[0], "image", image[1]))
                worktext = parts[2]
            if worktext != "":
                new_nodes.append(TextNode(worktext, "text"))
        else:
            new_nodes.append(node)
    else:
        new_nodes.append(node)

    new_nodes.extend(split_nodes_images(old_nodes[1:]))
    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []

    if len(old_nodes) == 0:
        return []

    try:
        node = old_nodes[0]
        node_text = node.text
        node_text_type = node.text_type
    except:
        raise TypeError(f"{old_nodes[0]}is not a TextNode")

    if node_text_type == "text":
        worktext = node_text
        extracted = extract_markdown_links(node_text)
        if len(extracted) > 0:
            for link in extracted:
                md = f"[{link[0]}]({link[1]})"
                parts = worktext.partition(md)
                if parts[0] != "":
                    new_nodes.append(TextNode(parts[0], "text"))
                new_nodes.append(TextNode(link[0], "link", link[1]))
                worktext = parts[2]
            if worktext != "":
                new_nodes.append(TextNode(worktext, "text"))
        else:
            new_nodes.append(node)
    else:
        new_nodes.append(node)

    new_nodes.extend(split_nodes_links(old_nodes[1:]))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, "text")]
    delimiters = (("**", "bold"), ("*", "italic"), ("`", "code"))
    for delimiter, type in delimiters:
        nodes = split_nodes_delimiter(nodes, delimiter, type)
    return split_nodes_links(split_nodes_images(nodes))
