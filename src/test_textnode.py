import unittest

from textnode import TextNode
from textnode import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestTextNode(unittest.TestCase):
    def test_create_url_optional(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, "bold")
        self.assertIsNone(node.url)

    def test_create_with_url(self):
        node = TextNode("This is an image node", "link", "http://example.com/test.jpg")
        self.assertEqual(node.text, "This is an image node")
        self.assertEqual(node.text_type, "link")
        self.assertEqual(node.url, "http://example.com/test.jpg")

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is an image node", "link", "http://example.com/test.jpg")
        self.assertNotEqual(node, node2)

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_textsplit_codeblock(self):
        node = TextNode("This is text with a `code block` word", "text")
        res = [TextNode("This is text with a ", "text"), TextNode("code block", "code"), TextNode(" word", "text")]
        self.assertListEqual(split_nodes_delimiter([node], "`", "code"), res)

    def test_textsplit_bold(self):
        node = TextNode("This is text with a **bolded** word", "text")
        res = [TextNode("This is text with a ", "text"), TextNode("bolded", "bold"), TextNode(" word", "text")]
        self.assertListEqual(split_nodes_delimiter([node], "**", "bold"), res)

    def test_textsplit_italic(self):
        node = TextNode("This is text with a *italicized* word", "text")
        res = [TextNode("This is text with a ", "text"), TextNode("italicized", "italic"), TextNode(" word", "text")]
        self.assertListEqual(split_nodes_delimiter([node], "*", "italic"), res)

    def test_textsplit_notextnode(self):
        with self.assertRaises(TypeError):
            split_nodes_delimiter(["fake TextNode"], "*", "italic")

    def test_textsplit_nolist(self):
        with self.assertRaises(TypeError):
            split_nodes_delimiter("fake TextNode", "**", "bold")

    def test_unclosed_symbols(self):
        node = TextNode("This is text with an uneven **bold symbol", "text")
        with self.assertRaises(SyntaxError):
            split_nodes_delimiter([node], "**", "bold")

    def test_multi_symbols(self):
        node = TextNode("**Double** the **boldness**", "text")
        res = [TextNode("Double", "bold"), TextNode(" the ", "text"), TextNode("boldness", "bold")]
        self.assertListEqual(split_nodes_delimiter([node], "**", "bold"), res)

class TestImageLinks(unittest.TestCase):
    def test_md_images(self):
        text = "This is text with an ![image](https://example.com/image1.png) and ![another](https://example.com/image2.jpg)"
        ans = [("image", "https://example.com/image1.png"), ("another", "https://example.com/image2.jpg")]
        self.assertListEqual(extract_markdown_images(text), ans)

    def test_md_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        ans = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertListEqual(extract_markdown_links(text), ans)

if __name__ == "__main__":
    unittest.main()
