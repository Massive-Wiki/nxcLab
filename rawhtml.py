#!/usr/bin/env python3

"""
simple html literal test for mistletoe
"""

from mistletoe import Document
from mistletoe.html_renderer import HtmlRenderer
from mistletoe.span_token import SpanToken

import re
# Set up logging
import logging, os
logging.basicConfig(level=os.environ.get('LOGLEVEL','INFO').upper())

class RawHtml(SpanToken):
    pattern = re.compile(r"\{\< ([^>]*) \>\}")

    def __init__(self, match):
        logging.info(f"RawHtml match: {match}")

class RawHtmlRenderer(HtmlRenderer):
    def __init__(self):
        super().__init__(RawHtml)
        logging.info("RawHtmlRendered initialized")

    def render_raw_html(self, token):
        logging.info(f"render_rawhtml token: {token}")
        template = '<{inner}>'
        inner = self.render_inner(token)
        return template.format(inner=inner)
    
def render_with_rawhtml(markdown):
    logging.info(f"render_with_rawhtml markdown: {markdown}")
    with RawHtmlRenderer() as renderer:
        return renderer.render(Document(markdown))
    
def main():
# Test the extension
    markdown_text = """
# Example 1

{< div class="navlink" >}

- [Home](README)
- [[Jankifiers]]

{< /div >}

## Example 2

{< p style="color:red;" >}
This is red!
{< /p >}
    """
    rendered_html = render_with_rawhtml(markdown_text)
    print("rendered html:\n", rendered_html)
    
if __name__ == '__main__':
    exit(main())
