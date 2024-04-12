import unittest

from textnode import TextNode


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

if __name__ == "__main__":
    unittest.main()
