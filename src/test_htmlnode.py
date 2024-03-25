import unittest
from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):

    def test_to_html_props(self):
        node = HTMLNode("div", "Hello World", None, {"class": "greetings"})
        self.assertEqual(node.props_to_html, ' class="greetings"')
    
    def test_to_html_no_children(self):
        node = LeafNode("h1", "Hello World!")
        self.assertEqual(node.to_html(), "<h1>Hello World</h1>")


if __name__ == "__main__":
    unittest.main()
