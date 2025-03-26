def get_book_text (path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def count_words (pathf):
    texto = get_book_text(pathf)
    count = 0
    for i in texto.split():
        count += 1
    return count

def character_count (pathf):
    texto = get_book_text(pathf)
    texto = texto.lower()
    setfinal = set(texto)
    letters = {}
    for item in setfinal:
        letters[item] = 0
#    letters = dict(sorted(letters.items()))
    for letter in texto:
        count = letters[letter]
        count += 1
        letters[letter] = count
    return letters

def sort_on(dicio):
    return dicio["value"]

def sort_dicio (dicio):
    lista = []
    dicio2 = {}
    for key, value in dicio.items():
        lista.append({"letter" : key, "value" : value})
    lista.sort(reverse=True, key=sort_on)
    for item in lista:
        dicio2[item["letter"]] = item["value"]
    return dicio2