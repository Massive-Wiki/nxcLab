from mistletoe import Document
from mistletoe.html_renderer import HtmlRenderer
from mistletoe.span_token import SpanToken
from mistletoe.block_token import BlockToken

import re
# Set up logging
import logging, os
logging.basicConfig(level=os.environ.get('LOGLEVEL','INFO').upper())
logger = logging.getLogger(__name__)

class CurlybraceTag(BlockToken):
    pattern = re.compile(r'\{\<\s([^>]*)\s\>\}')

    def __init__(self, match):
        logger.info(f"CurlybraceTag match: {match}")
        self.target = match
        
    @staticmethod
    def start(line):
        return CurlybraceTag.pattern.match(line) is not None
    
class CurlybraceTagRenderer(HtmlRenderer):
    def __init__(self):
        super().__init__(CurlybraceTag)

    def render_curlybrace_tag(self, token):
        logger.debug(f"render_curlybrace_tag token: {token}")
        logger.info(f"token target: {token.target}")
        template = '<{target}>'
        target = token.target
        return template.format(target=target)
    
def render_with_curlybraces(markdown):
    logger.info(f"render_with_curlybraces markdown: {markdown}")
    with CurlybraceTagRenderer() as renderer:
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
    rendered_html = render_with_curlybraces(markdown_text)
    print("rendered html:\n", rendered_html)
    
if __name__ == '__main__':
    exit(main())
