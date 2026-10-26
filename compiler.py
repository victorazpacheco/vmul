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


    content = content.replace("$HASHTAG", "#")
    content = content.replace("$DOUBLEHASHTAG", "##")
    content = content.replace("$ASTERISK", "*")
    content = content.replace("$DOUBLEASTERISK", "**")
    content = content.replace("$HYPHEN", "-")
    content = content.replace("$UNDERLINE", "_")
    content = content.replace("$EXCLAMATIONMARK", "!")
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
