# rawhtml

## RawHtml Blocks  

RawHtml Blocks is a Markdown extension that supports embedding HTML elements and associated attributes in Markdown files.

A RawHtml Block is a sequence that starts with an opening character pattern consisting of a curly-brace ('{'), followed by a less-than symbol ('<'), and a single space (' '): `{< `. This sequence is followed by an HTML tag, and any specified attributes. The pattern is closed with the following character sequence: ` >}` (a single space (' ') followed by a greater-than symbol ('>') and a closing curly-brace ('}'), terminated with a newline.

The inner content of the RawHtml block consists of all subsequent lines, up to, but not including, a closing curlybrace tag element.

A RawHtml block may interrupt a paragraph. 
Q: is a blank line required before or after a curlybrace sequence?

The inner content of a RawHtml block is rendered as Markdown.

