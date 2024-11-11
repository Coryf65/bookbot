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


def sort_on(dict):
  '''
    This is used to sort the dictionary in sort_dictionary to sort by the count of chars
  '''
  print(dict)
  return [1]


def sort_dictionary(unsorted_dict, reversed = True):
  sorted_dict = sorted(unsorted_dict.items(), key=lambda x:x[1], reverse=reversed)
  converted_dict = dict(sorted_dict)
  return converted_dict


# The main loop
def main():
   book_path = "books/frankenstien.txt"
   book_data = read_book_from_file(book_path)
   word_count = count_words(book_data)
   print(f"-- Begin report of '{book_path}' ---")
   print(f"{word_count} words found in the document")
   print()
   
   characters = count_characters(book_data)
   sorted_characters = sort_dictionary(characters, reversed=True)
   
   for item in sorted_characters:
     if item.isalpha(): 
      print(f"The '{item}' character was found '{sorted_characters[item]}' times")   

if __name__ == '__main__':
  main()