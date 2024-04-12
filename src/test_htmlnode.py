import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_create(self):
        node = HTMLNode("h1", "a html title", None, {"color": "red"})
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "a html title")
        self.assertIsNone(node.children)
        self.assertEqual(node.props["color"], "red")

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_empty_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
    def test_create_none(self):
        with self.assertRaises(ValueError):
            LeafNode(None)

    def test_create_empty_string(self):
        with self.assertRaises(ValueError):
            LeafNode("")

    def test_no_tag(self):
        node = LeafNode("Just a value with no tag")
        self.assertEqual(node.to_html(), "Just a value with no tag")

    def test_tag(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_tag_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()
