def replace(content):
    content = content.replace("\**", "</b>")
    content = content.replace("**", "<b>")
    content = content.replace("\*", "</i>")
    content = content.replace("*", "<i>")
    content = content.replace("\%", "</var>")
    content = content.replace("%", "<var>")
    content = content.replace("$\n", "<br>")
    content = content.replace("\##", "</h2>")
    content = content.replace("##", "<h2>")
    content = content.replace("\#", "</h1>")
    content = content.replace("#", "<h1>")
    content = content.replace("$FULLBAR", "<meter value='1'></meter>")
    content = content.replace("$SEMIBAR", "<meter value='0.5'></meter>")
    content = content.replace("$ZEROBAR", "<meter value='0'></meter>")
    content = content.replace("\-", "</s>")
    content = content.replace("-", "<s>")
    content = content.replace("\_", "</u>")
    content = content.replace("_", "<u>")
    content = content.replace("$===", "<hr>")
    content = content.replace("\!", "</title>")
    content = content.replace("!", "<title>")
    content = content.replace("$ENDATTRIBUTES", '"')
    content = content.replace("$QUOTE", "'")
    content = content.replace("$DOUBLEQUOTE", '"')
    content = content.replace("$SRC", 'src="')
    content = content.replace("$CLOSEENDTAG", ">")
    content = content.replace("$CLOSETAG", ">")
    content = content.replace("$OPENENDTAG", "</")
    content = content.replace("$OPENTAG", "<")
    content = content.replace("$HASHTAG", "#")
    content = content.replace("$DOUBLEHASHTAG", "##")
    content = content.replace("$ASTERISK", "*")
    content = content.replace("$DOUBLEASTERISK", "**")
    content = content.replace("$HYPHEN", "-")
    content = content.replace("$UNDERLINE", "_")
    content = content.replace("$EXCLAMATIONMARK", "!")
    content = content.replace("$HTTPS", "https://")
    content = content.replace("$HTTP", "http://")
    content = content.replace("$FTP", "ftp://")
    content = content.replace("$SFTP", "sftp://")
    content = content.replace("@HTML", "html")
    content = content.replace("@H1", "h1")
    content = content.replace("@H2", "h2")
    content = content.replace("@BODY", "body")
    content = content.replace("$\t", "  ")
    content = content.replace("@TITLE", "title")
    content = content.replace("@B", "b")
    content = content.replace("@I", "i")
    content = content.replace("@IMG", "img")
    content = content.replace("@HEAD", "head")
    content = content.replace("@BUTTON", "button")
    content = content.replace("$ONCLICK", 'onclick="')
    content = content.replace("$ID", 'id="')
    content = content.replace("$CLASS", 'class="')
    content = content.replace("$WIDTH", 'width="')
    content = content.replace("$HEIGHT", 'width="')
    content = content.replace("$SPAN", 'span')
    content = content.replace("@EM", 'em')
    content = content.replace("@VAR", 'var')
    return content
def main():
    file_dir = input("File dir (.vmul): ")
    compile_to = input("Compile to (html): ")
    if not file_dir or file_dir == "":
        file_dir = "file.vmul"
    if not compile_to or compile_to == "":
        compile_to = "index.html"
    try:
        with open(file_dir, 'r', encoding='utf-8') as f:
            if f:
                content = f.read()
            else:
                content = "<h1>Nothing Found</h1>"
    except FileNotFoundError:
        print(f"File {file_dir} not found")
        content = "<h1>Nothing Found</h1>"
    except Exception:
        content = "<h1>Unknown Error</h1>"
        raise("Unknown error")
    content = replace(content)
    try:
        with open(compile_to, 'w', encoding='utf-8') as f:
            f.write(content)
    except FileNotFoundError:
        print(f"File {compile_to} not found")
main()
