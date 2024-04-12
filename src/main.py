from textnode import TextNode

def main():
    bold = TextNode("testing", "bold")
    print(bold)
    image = TextNode("testing image", "link", "http://example.com/test.jpg")
    print(image)
    clone = TextNode("testing image", "link", "http://example.com/test.jpg")

    if image == clone:
        print("Image and it's clone are equal")
    else:
        print("Image and it's clone are not equal")


main()
