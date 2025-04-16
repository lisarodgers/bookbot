import sys
from stats import word_count, count_characters, analyze_book

def get_book_text(filepath):
   with open(filepath, 'r', encoding='utf-8') as file:    
        return file.read()

def main():
     # ✅ Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_contents = get_book_text(sys.argv[1])
    num_words = word_count(book_contents)
    num_char = count_characters(book_contents)
    analyze_book(sys.argv[1],num_words,num_char)
# Call the main function to run the program
main()