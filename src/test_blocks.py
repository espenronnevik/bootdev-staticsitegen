import unittest

from blocks import markdown_to_blocks

class TestBlockFuncs(unittest.TestCase):
    def test_markdown_to_blocks_example(self):
        text = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        self.assertEqual(len(markdown_to_blocks(text)), 3)

    def test_markdown_to_blocks_single(self):
        text = "This is a **single** block of text"
        self.assertEqual(len(markdown_to_blocks(text)), 1)

    def test_markdown_to_blocks_empty(self):
        text = "This is **two** blocks of text\n\n\n\n\n\n\n\nWith excessive newlines in between"
        self.assertEqual(len(markdown_to_blocks(text)), 2)
