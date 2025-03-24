import unittest
from stats import get_num_words
import main

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_get_num_words(self):
        book_path = '/mnt/sda1/Code/_Courses/Boot.Dev/project-1-python-bookbot/bookbot/books/mobydick.txt'
        book_data = main.read_book_from_file(book_path)
        wordsCount = get_num_words(book_data)
        print(wordsCount)
        characters = main.count_characters(book_data)
        print(characters)
        self.assertTrue(1)


if __name__ == '__main__':
    unittest.main()