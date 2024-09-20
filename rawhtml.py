#!/usr/bin/env python3

from mistletoe import Document
from mistletoe.html_renderer import HtmlRenderer
from mistletoe.block_token import BlockToken
import re

# Set up logging
import logging, os
logging.basicConfig(level=os.environ.get('LOGLEVEL','INFO').upper())
logger = logging.getLogger(__name__)

#setup argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Experiments with raw html rendering')
    parser.add_argument('--input', '-i', required=False, help='path to example/test markdown file')
    return parser

class RawHtml(BlockToken):
    pattern = re.compile(r'\{\< ([^>]*) \>\}')

    def __init__(self, match):
        logger.info(f"RawHtml match: {match}")
        self.target = match
        
    @staticmethod
    def start(line):
        return RawHtml.pattern.match(line) is not None
    
class RawHtmlRenderer(HtmlRenderer):
    def __init__(self):
        super().__init__(RawHtml)

    def render_raw_html(self, token):
        logger.debug(f"render_raw_html token: {token}")
        logger.info(f"token target: {token.target}")
        if len(token.target) == 1:
            target = token.target[0].replace('{< ','<').replace(' >}\n','>')
        else:
            target = token.target
        template = '{target}'
        return template.format(target=target)
    
def render_with_rawhtml(markdown):
    logger.info(f"render_with_rawhtml markdown: {markdown}")
    with RawHtmlRenderer() as renderer:
        return renderer.render(Document(markdown))
    
def main():
    argparser = init_argparse()
    args = argparser.parse_args()
    logger.debug(f"parsed args: {args}")

    example_input = 'nxc_ex3.md'
    if args.input:
        example_input = args.input
    with open(example_input, 'r', encoding="utf-8") as f:
        markdown_text = f.read()
    logger.debug(f"markdown text: {markdown_text}")
    rendered_html = render_with_rawhtml(markdown_text)
    print(f"the rendered html:\n{rendered_html}")

# Test the extension
    inline_text = """
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
    rendered_html = render_with_rawhtml(inline_text)
    print("the inline text rendered html:\n", rendered_html)
    
if __name__ == '__main__':
    exit(main())
