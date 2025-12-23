import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraph_blocks(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_md_to_code_block(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )



    def test_quote_block(self):
        md = """
            The quote

            > Somewhere, something incredible is waiting to be known

            has been ascribed to Carl Sagan.
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>The quote</p><blockquote>Somewhere, something incredible is waiting to be known</blockquote><p>has been ascribed to Carl Sagan.</p></div>", 
        )
    
    def test_ul_block(self):
        md = """The shopping list:

        - bread
        - milk
        - potato chips

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>The shopping list:</p><ul><li>bread</li><li>milk</li><li>potato chips</li></ul></div>", 
        )
    
    def test_ol_block(self):
        md = """The shopping list:

        1. garlic bread
        2. soy milk
        3. vegan potato chips

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>The shopping list:</p><ol><li>garlic bread</li><li>soy milk</li><li>vegan potato chips</li></ol></div>", 
        )
    
    def test_heading_blocks(self):
        md = """
        # esto es un h1

        ## esto es un h2

        ### esto es un h3

        #### esto es un h4

        ##### esto es un h5

        ###### esto es un h6
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>esto es un h1</h1><h2>esto es un h2</h2><h3>esto es un h3</h3><h4>esto es un h4</h4><h5>esto es un h5</h5><h6>esto es un h6</h6></div>",  
        )
    



if __name__ == "__main__":
    unittest.main()