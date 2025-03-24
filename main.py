#!/usr/bin/python3
import sys
from stats import get_num_words


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


def sort_dictionary(unsorted_dict, reversed = True):
  '''
    Sort a Disctionary by using a lamda.
    
    Args:
      unsorted_dict: The dictionary to sort
      reversed: True = sorts in descending order, big to small, False = sorts in ascending order, small to big 
    
    Returns:
      A dictionary sorted.
  '''
  sorted_dict = sorted(unsorted_dict.items(), key=lambda x:x[1], reverse=reversed)
  converted_dict = dict(sorted_dict)
  return converted_dict


# The main loop
def main():
  book_path = "books/frankenstein.txt"
  book_data = read_book_from_file(book_path)
  word_count = get_num_words(book_data)
    
  print(f"-- Begin report of '{book_path}' ---")
  print(f"{word_count} words found in the document")
  print()
     
  characters = count_characters(book_data)
  sorted_characters = sort_dictionary(characters, reversed=True)
   
  for item in sorted_characters:
    if item.isalpha(): 
      print(f"The '{item}' character was found '{sorted_characters[item]}' times")
  
  print("--- end of report ---")

if __name__ == '__main__':
  main()