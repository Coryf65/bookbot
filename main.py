#!/usr/bin/python3

# import modules used here -- sys is a very standard one
import sys


# read file and print text
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

    # need to lood through every character and count
    for character in text:
      print(character)
      all_characters[character] = all_characters[character]   
      print(all_characters[character]) 
    return text


# Gather our code in a main() function
def main():
   book_path = "books/frankenstien.txt"
   book_data = read_book_from_file(book_path)
   #print(book_data)
   word_count = count_words(book_data)
   print(f"{word_count} words found in the document")
   
   count_characters("cory test one two")

if __name__ == '__main__':
  main()