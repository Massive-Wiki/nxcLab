import re
from mistletoe.block_token import BlockToken
from mistletoe.html_renderer import HtmlRenderer

class CustomToken(BlockToken):
    """
    Custom token for handling content between '{< tag' and '{< /tag >}' patterns.
    """

    start_pattern = re.compile(r'^\s*\{<\s*(\w+)')
    end_pattern = re.compile(r'^\s*\{<\s*/(\w+)\s*>\}')

    def __init__(self, tag, content):
        self.tag = tag
        self.content = content

    @staticmethod
    def start(line):
        return CustomToken.start_pattern.match(line) is not None

    @classmethod
    def read(cls, lines):
        first_line = next(lines)
        match = cls.start_pattern.match(first_line)
        if not match:
            raise ValueError("Invalid start of CustomToken")

        tag = match.group(1)
        content = []
        
        for line in lines:
            end_match = cls.end_pattern.match(line)
            if end_match and end_match.group(1) == tag:
                break
            content.append(line)

        return cls(tag, content)

    def __repr__(self):
        return f"CustomToken(tag='{self.tag}', content={self.content})"

class CustomTokenRenderer(HtmlRenderer):
    def __init__(self):
        super().__init__(CustomToken)

    def render_custom_token(self,token):
        print(f"render c t token: {token}")
        return 'we were called'

