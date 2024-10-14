def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = word_count(text)

    num_chars = char_count(text)
    char_list = dict_to_list_of_dicts(num_chars)
    char_list.sort(reverse=True, key=sort_on)

    print(f"-- Begin report on {book_path} --")
    print(f"Number of words found in {book_path}: {num_words}\n")

    for i in char_list:
        ch = i["char"]
        count = i["count"]
        print(f"The character {ch} was found {count} times")

    print("-- End report --")

# reads text into a string
def get_text(path:str):
    with open("books/frankenstein.txt") as f:
        return f.read()

# returns word count
def word_count(text:str):
    return len(text.split())

# returns dict of character counts
def char_count(text:str):
    lower = text.lower()
    charmap = {}

    for c in lower:
        if c in charmap:
            charmap[c] += 1
        else:
            charmap[c] = 1

    return charmap

# converts dict of char counts into list of dicts for sorting purposes
def dict_to_list_of_dicts(num_chars:dict):
    char_list = []

    for k, v in num_chars.items():
        tmp = {}
        if k.isalpha():
            tmp["char"] = k
            tmp["count"] = v
            char_list.append(tmp)

    return char_list


def sort_on(dict):
    return dict["count"]

main()