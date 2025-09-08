def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    d = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d


def dict_to_list(dict_char_counts):
    list_char_counts = []
    for key, value in dict_char_counts.items():
        list_char_counts.append({"name":key, "num":value})

    # A function that takes a dictionary and returns the value of the "num" key
    # This is how the `.sort()` method knows how to sort the list of dictionaries
    def sort_on(items):
        return items["num"]

    list_char_counts.sort(reverse=True, key=sort_on)

    return list_char_counts

