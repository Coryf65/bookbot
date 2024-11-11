#!/usr/bin/python3

# import modules used here -- sys is a very standard one
import sys


# read file and print text
def read_book_from_file(path):
    file_contents = ""

    with open(path) as f:
        file_contents = f.read()

    return file_contents


def count_words(text):
   split = text.split()
   return len(split)
   

# Gather our code in a main() function
def main():
   book_path = "books/frankenstien.txt"
   book_data = read_book_from_file(book_path)
   #print(book_data)
   word_count = count_words(book_data)
   print(f"{word_count} words found in the document")

if __name__ == '__main__':
  main()