# rawhtml
\# $Id$

## RawHtml Blocks  

RawHtml Blocks is a Mistletoe extension that supports embedding HTML block-level elements and associated attributes in Markdown files.

A RawHtml Block begins with a single line that starts with an opening character sequence consisting of a curly-brace ('{'), followed by a less-than symbol ('<'), and a single space (' '): `{< `. This sequence is followed by an HTML block-level element tag, and any specified attributes. The RawHtml block is closed with a single line that starts with the following character sequence: a single space (' ') followed by a greater-than symbol ('>') and a closing curly-brace ('}') (` >}`).

The inner content of the RawHtml block consists of all subsequent lines, up to, but not including, a single line containing the closing tag element statement; e.g., `{< /tag >}`. The inner content of a RawHtml block is processed as Markdown.

For example, the following text:
```
## example with lists and links

{< div class="navlink" >}
- [Home](/README.html)
- Jankifiers
{< /div >}
```

is rendered by (extended) Mistletoe as:
```
<h2>example with lists and links</h2>
<div class="navlink">
<ul>
<li><a href="/README.html">Home</a></li>
<li>Jankifiers</li>
</ul>
</div>
```


