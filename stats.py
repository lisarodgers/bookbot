def word_count(string):
    words = string.split()
    return len(words)

def count_characters(string):
     string = string.lower()  # normalize to lowercase
     char_counts = {}

     for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

     return char_counts

def sort_characters(char_dict):
    # Create a list of {"char": c, "count": n} dicts
    sorted_list = [{"char": char, "count": count} for char, count in char_dict.items()]
    # Sort in-place by count, descending
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list

def analyze_book(book_path,num_words,char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----")
    
    sorted_chars = sort_characters(char_dict)
    for entry in sorted_chars:
        char = entry["char"]
        count = entry["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    return

