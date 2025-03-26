from stats import count_words, character_count, sort_dicio
import sys

def main ():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    pathf = sys.argv[1]
    num = count_words(pathf)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {pathf}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    letras = character_count(pathf)
    letras = sort_dicio(letras)
    for key, value in letras.items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
    return



main()
