from re import match, findall

block_type_paragraph      = "paragraph"
block_type_heading        = "heading"
block_type_code           = "code"
block_type_quote          = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list   = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    for line in markdown.split("\n\n"):
        if line != "":
            blocks.append(line.strip())
    return blocks

def validate_order(lines, num=1):
    if len(lines) == 0:
        return True

    snum = lines[0].split(".")[0]
    res =  int(snum) == num
    return res and validate_order(lines[1:], num + 1)

def block_to_block_type(text):
    re_heading = r"^#{1,6} "
    re_code = r"(?s)^```.*```$"
    re_quote = r"(?m)^(>)"
    re_unordered_list = r"(?m)^(\*|-) "
    re_ordered_list = r"(?m)^(\d+)\. "

    type = block_type_paragraph
    lines = text.split("\n")
    if match(re_heading, text) is not None:
        type = block_type_heading
    elif match(re_code, text) is not None:
        type = block_type_code
    elif len(findall(re_quote, text)) == len(lines):
        type = block_type_quote
    elif len(findall(re_unordered_list, text)) == len(lines):
        type = block_type_unordered_list
    elif len(findall(re_ordered_list, text)) == len(lines) and validate_order(lines):
        type = block_type_ordered_list
    return type
