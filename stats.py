def get_num_words(text):
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