import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_create(self):
        node = HTMLNode("h1", "a html title", None, {"color": "red"})
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "a html title")
        self.assertIsNone(node.children)
        self.assertEqual(node.props["color"], "red")

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()
