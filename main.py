#!/usr/bin/python3
import sys


def read_book_from_file(path):
  '''
		Reads the contents of a text file (book text) and returns it.

    Args:
			path (string): The path to the file to read.

		Returns:
			string: all of the text in the given file.
  '''
  file_contents = ""
  with open(path) as f:
    file_contents = f.read()
  
  return file_contents


def count_words(text):
  '''
    Counts the total number of words and returns the counter.
    uses a space as the delimeter.

    Args:
        text (string): The text to parse.

    Returns:
        int: The total number of words counted.
   '''
  split = text.split()
  return len(split)


def count_characters(text):
    '''
     Counts the total number of characters used and 
     returns a dictionary with each letter and how many times it occured.

    Args:
        text (string): The text to parse.

    Returns:
        {'p': 6121, 'r': 20818 }: returns a dictionary with each letter and how many times it occured.
    '''
    all_characters = {}
    # need to loop through every character and count
    for character in text.lower():
      if character in all_characters:
        # up by one
        all_characters[character] += 1
      else:
        all_characters[character] = 1
    return all_characters


# The main loop
def main():
   book_path = "books/frankenstien.txt"
   book_data = read_book_from_file(book_path)
   print(book_data)
   word_count = count_words(book_data)
   print(f"{word_count} words found in the document")
   characters = count_characters(book_data)
   print(f"total characters used in this book: {characters}")

if __name__ == '__main__':
  main()