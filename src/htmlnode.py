from blocks import block_type_heading, block_type_code, block_type_quote, \
    block_type_unordered_list, block_type_ordered_list
from blocks import markdown_to_blocks, block_to_block_type


class HTMLNode(object):
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

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


def paragraph_to_htmlnode(block):
    return HTMLNode("p", block)


def heading_to_htmlnode(block):
    parts = block.split()
    return HTMLNode(f"h{len(parts[0])}", " ".join(parts[1:]))


def quote_to_htmlnode(block):
    parts = []
    for line in block.split("\n"):
        parts.append(line[1:].lstrip())
    return HTMLNode("quoteblock", "\n".join(parts))


def code_to_htmlnode(block):
    return HTMLNode("pre", None, [HTMLNode("code", block[3:][:-3])])


def unordered_list_to_htmlnode(block):
    listitems = []
    for line in block.split("\n"):
        listitems.append(HTMLNode("li", line[1:].lstrip()))
    return HTMLNode("ul", None, listitems)


def ordered_list_to_htmlnode(block):
    listitems = []
    for line in block.split("\n"):
        listitems.append(HTMLNode("li", line.split(". ", 1)[1]))
    return HTMLNode("ol", None, listitems)


def markdown_to_htmlnode(markdown):
    nodes = []
    for block in markdown_to_blocks(markdown):
        type = block_to_block_type(block)
        if type == block_type_heading:
            node = heading_to_htmlnode(block)
        elif type == block_type_quote:
            node = quote_to_htmlnode(block)
        elif type == block_type_code:
            node = code_to_htmlnode(block)
        elif type == block_type_unordered_list:
            node = unordered_list_to_htmlnode(block)
        elif type == block_type_ordered_list:
            node = ordered_list_to_htmlnode(block)
        else:
            node = paragraph_to_htmlnode(block)
        nodes.append(node)
    return HTMLNode("div", None, nodes)
