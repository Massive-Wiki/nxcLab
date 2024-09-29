# rawhtml in markdown test note
 - this note contains some mix of `nxc` `rawhtml` markup and Markdown text.
   - one test is whether these patterns can be handled in `MassiveWikiRenderer`

## example 1

Some text before

{< div class="example" id="test" >}
Line 1 inside the div  
Line 2 inside the div  
Line 3 inside the div  
{< /div >}

Some text after

{< section >}
A section content; and
more content  
Enough, already.
{< /section >}

## example with lists and links

{< div class="navlink" >}
- [Home](/README.html)
- [[Jankifiers]]
{< /div >}

## inline span test
 - This text, is <span style="color:red;">_special_</span>, and is
   rendered just fine!  


