from mistletoe import Document
from mistletoe.html_renderer import HtmlRenderer
from mistletoe import block_token, span_token
import re

# Set up logging
import logging, os
logging.basicConfig(level=os.environ.get('LOGLEVEL','INFO').upper())
logger = logging.getLogger(__name__)

class NXCHtml(block_token.BlockToken):
    """
    NXCHtml token. ?
    """
#    pattern = re.compile(r"(?s)\{< div ([^<]*) >\}\n(.*?)\n\{< /div >\}")
    pattern = r"\{<\s*([a-z]+)\s*[^>]*\>\}(?:\n|.)*?\{<\s*/\1\s*\>\}"
    def __init__(self, match):
        logger.info(f"NXCHtml match: {match}")

    @property
    def content(self):
        return self.children[0].content
    
    @staticmethod
    def start(line):
        return line

class NXCHtmlRenderer(HtmlRenderer):
    def __init__(self):
        super().__init__(NXCHtml)
        logger.info("NXCHtmlRendered initialized")

    def render_nxc_html(self, token):
        logger.info(f"render_nxchtml token: {token}")
#        logger.info(f"token target: {token.target}")
#        template = '{inner}>'
#        inner = self.render_inner(token)
#        return template.format(inner=inner)
        return 'we have nothing'
    
def render_with_nxchtml(markdown):
    logger.info(f"render_with_nxchtml markdown: \n{markdown}")
    with NXCHtmlRenderer() as renderer:
        return renderer.render(Document(markdown))
    
def main():
#    argparser = init_argparse()
#    args = argparser.parse_args()
#    logger.debug(f"parsed args: {args}")

    nxchtml_input = 'nxc_ex3.md'
#    if args.input:
#        rawhtml_input = args.input
    with open(nxchtml_input, 'r', encoding="utf-8") as f:
        markdown_text = f.read()
    logger.debug(f"markdown text: {markdown_text}")
    rendered_html = render_with_nxchtml(markdown_text)
    print(f"the rendered html:\n{rendered_html}")
    
if __name__ == '__main__':
    exit(main())
