#!/usr/bin/python3

# import modules used here -- sys is a very standard one
import sys


# read file and print text
def ReadBookFile(path):
    file_contents = ""

    with open(path) as f:
        file_contents = f.read()

    return file_contents


# Gather our code in a main() function
def main():
   book_path = "books/frankenstien.txt"
   book_data = ReadBookFile(book_path)
   print(book_data)

if __name__ == '__main__':
  main()