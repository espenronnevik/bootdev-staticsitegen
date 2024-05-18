import unittest

from blocks import block_type_paragraph, block_type_heading, block_type_code, block_type_quote, \
    block_type_unordered_list, block_type_ordered_list
from blocks import markdown_to_blocks, block_to_block_type


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

    def test_block_to_block_type_paragraph(self):
        text = "This is just a normal paragraph"
        self.assertEqual(block_to_block_type(text), block_type_paragraph)

    def test_block_to_block_type_heading(self):
        valid = "### A Level 3 header"
        invalid = "No header here"
        fake = "This appears to contain headers\n# But it does not"
        self.assertEqual(block_to_block_type(valid), block_type_heading)
        self.assertEqual(block_to_block_type(invalid), block_type_paragraph)
        self.assertEqual(block_to_block_type(fake), block_type_paragraph)

    def test_block_to_block_type_code(self):
        valid_single = "``` Valid single line code block ```"
        valid_multi = "```This is a valid\nMultiline code block```"
        invalid = "``This only contains two backticks``"
        unbalanced = "```Valid beginning tag\nbut it in unbalanced and missing end tag"
        self.assertEqual(block_to_block_type(valid_single), block_type_code)
        self.assertEqual(block_to_block_type(valid_multi), block_type_code)
        self.assertEqual(block_to_block_type(invalid), block_type_paragraph)
        self.assertEqual(block_to_block_type(unbalanced), block_type_paragraph)

    def test_block_to_block_type_quote(self):
        valid_single = "> This is one liner"
        valid_multi = "> Quote spanning\n>over several\n>lines"
        fake = "The character should not > appear in the middle"
        invalid_multi = "> All lines \n>should contain\na > character at the start"
        self.assertEqual(block_to_block_type(valid_single), block_type_quote)
        self.assertEqual(block_to_block_type(valid_multi), block_type_quote)
        self.assertEqual(block_to_block_type(fake), block_type_paragraph)
        self.assertEqual(block_to_block_type(invalid_multi), block_type_paragraph)

    def test_block_to_block_type_unordered_list(self):
        valid_single_var1 = "* This is one version"
        valid_single_var2 = "- This is another version"
        valid_mixed = "* Mixing and matching\n- variants is possible"
        valid_multi_long = "* A big \n* unordered\n* List\n* With many lines"
        invalid = "- Every line must contain\n a list character"
        self.assertEqual(block_to_block_type(valid_single_var1), block_type_unordered_list)
        self.assertEqual(block_to_block_type(valid_single_var2), block_type_unordered_list)
        self.assertEqual(block_to_block_type(valid_mixed), block_type_unordered_list)
        self.assertEqual(block_to_block_type(valid_multi_long), block_type_unordered_list)
        self.assertEqual(block_to_block_type(invalid), block_type_paragraph)

    def test_block_to_block_type_ordered_list(self):
        valid_single = "1. This is an ordered list"
        valid_multi = "1. First item\n2. Second item\n3. Third item"
        invalid_multi = "1. First item\n Second item\n3. Third item"
        invalid_order = "1. First item\n3. Second item\n2. Third item"
        self.assertEqual(block_to_block_type(valid_single), block_type_ordered_list)
        self.assertEqual(block_to_block_type(valid_multi), block_type_ordered_list)
        self.assertEqual(block_to_block_type(invalid_multi), block_type_paragraph)
        self.assertEqual(block_to_block_type(invalid_order), block_type_paragraph)
