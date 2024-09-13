#!/usr/bin/env python3

"""
simple raw html processing for mistletoe
"""

from mistletoe import Document
from mistletoe.html_renderer import HtmlRenderer
from mistletoe.span_token import SpanToken

import re
# Set up logging
import logging, os
logging.basicConfig(level=os.environ.get('LOGLEVEL','WARNING').upper())
logger = logging.getLogger(__name__)

class RawHtml(SpanToken):
    pattern = re.compile(r"\{\< ([^>]*) \>\}")

    def __init__(self, match):
        logger.debug(f"RawHtml match: {match}")

class RawHtmlRenderer(HtmlRenderer):
    def __init__(self):
        super().__init__(RawHtml)

    def render_raw_html(self, token):
        logger.debug(f"render_rawhtml token: {token}")
        template = '<{inner}>'
        inner = self.render_inner(token)
        return template.format(inner=inner)
    
def render_with_rawhtml(markdown):
    logger.info(f"render_with_rawhtml markdown: {markdown}")
    with RawHtmlRenderer() as renderer:
        return renderer.render(Document(markdown))
    
def main():
    with open('rawhtml_examples.md', 'r', encoding="utf-8") as f:
        markdown_text = f.read()
    logger.info(f"markdown text: {markdown_text}")
    rendered_html = render_with_rawhtml(markdown_text)
    logger.info(f"the rendered html:\n{rendered_html}")
    
if __name__ == '__main__':
    exit(main())
