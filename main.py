DEFAULT_STORY = "frankenstein"

def get_text(name:str):
    path_to_file = "./books/" + name + ".txt"
    with open(path_to_file) as f:
        return f.read()
    
def get_word_count(text:str):
    words = text.split()
    return len(words)

def get_letter_count(text:str):
    lowered_text = text.lower()
    res = {}
    for letter in lowered_text:
        if not letter.isalpha():
            continue
        res[letter] = res.get(letter, 0) + 1
    return res

def print_letter_count_desc(res:dict):
    print("--- Begin report of books/frankenstein.txt ---")
    for key, value in sorted(res.items(), key=lambda x: x[1], reverse=True):
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def main(name=DEFAULT_STORY):
    file_contents = get_text(name)
    word_count = get_word_count(file_contents)
    print(word_count)
    res = get_letter_count(file_contents)
    print_letter_count_desc(res)
    return None

main("frankenstein")
