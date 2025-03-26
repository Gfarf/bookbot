def get_book_text (path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def main ():
    pathf = "./books/frankenstein.txt"
    texto = get_book_text(pathf)
    count = 0
    for i in texto.split():
        count += 1
    print(f"{count} words found in the document")
    return

main()