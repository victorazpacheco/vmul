# Victor MarkUp Language (VMUL)

**VMUL** is a mark up programing language that's transpiled (compiled) to HTML. Here are some basic commands you can use in it (and their translations):

**Hashtag** -> h1 (title)
**Double Hashtag** -> h2 (smaller title)
**Double Asterisk** -> b (bold)

Single tag (on VMUL) items are written with a $ before it. Examples:

**$===** -> hr
**$\n** -> br
**$FULLBAR** -> meter value = "1"

You can also use characters that would be translated using $. Example:

**$HASHTAG** -> #
**$DOUBLEHASHTAG** -> ##
**$DOUBLEASTERISK** -> **

To use this VMUL compiler type your .vmul input file and your .html output file. Example:

$ File dir: file.vmul
$ Compile to: index.html
