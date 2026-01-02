
def get_book_text(book_path):
    with open(book_path) as file:
        contents = file.read()
    return contents

def get_num_words(contents: str):
    words = contents.split()
    word_count = len(words)
    return word_count

def get_character_count(contents: str):
    contents = contents.lower()
    inv = {}
    for c in contents:
        if inv.get(c) == None:
            inv[c] = 1
        else:
            inv[c]+=1
    return inv

def sort_character_list(inv: dict[str, int]):
    char_list = []
    for key,value in inv.items():
        char_list.append({"char": key, "num": value})
    char_list.sort(key=sort_on, reverse=True)
    return char_list

def sort_on(items):
    return items["num"]

def generate_report(book_path):
    contents = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(contents)} total words")
    print("--------- Character Count -------")
    character_dict = get_character_count(contents)
    sorted_character_list = sort_character_list(character_dict)
    for entry in sorted_character_list:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

