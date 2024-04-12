def markdown_to_blocks(markdown):
    blocks = []
    for line in markdown.split("\n\n"):
        if line != "":
            blocks.append(line.strip())
    return blocks
