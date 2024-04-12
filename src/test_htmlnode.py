import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_create_none_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("test")])

    def test_create_empty_tag(self):
        with self.assertRaises(ValueError):
            ParentNode("", [LeafNode("test")])

    def test_create_none_children(self):
        with self.assertRaises(ValueError):
            ParentNode("h1", None)

    def test_create_empty_children(self):
        with self.assertRaises(ValueError):
            ParentNode("h1", [])

    def test_basic_leafnodes(self):
        leafs = [
            LeafNode("Bold text", "b"),
            LeafNode("Normal text"),
            LeafNode("italic text", "i"),
            LeafNode("Normal text")
        ]
        node = ParentNode("p", leafs)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nested_list(self):
        text1 = [LeafNode("First", "b"), LeafNode(" list item")]
        text2 = [LeafNode("List item "), LeafNode("2", "i")]
        text3 = [LeafNode("List item "), LeafNode("3")]
        item1 = ParentNode("li", text1)
        item2 = ParentNode("li", text2)
        item3 = ParentNode("li", text3)
        node = ParentNode("ul", [item1, item2, item3])
        self.assertEqual(node.to_html(), "<ul><li><b>First</b> list item</li><li>List item <i>2</i></li><li>List item 3</li></ul>")

if __name__ == "__main__":
    unittest.main()
