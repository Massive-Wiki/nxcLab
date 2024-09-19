import logging, os
logging.basicConfig(level=os.environ.get('LOGLEVEL','INFO').upper())
logger = logging.getLogger(__name__)

from mistletoe.html_renderer import HtmlRenderer
from mistletoe import block_token, span_token
import re

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
#        template = '{inner}>'
#        inner = self.render_inner(token)
#        return template.format(inner=inner)
        return 'we have nothing'


