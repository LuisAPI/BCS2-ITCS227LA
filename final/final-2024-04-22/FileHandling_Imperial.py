# -*- coding: utf-8 -*-
"""FileHandling_Imperial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/151nnrDGjO2LRXvwAQfoPwutYLrh2jxGf
"""

# De La Salle University–Dasmariñas
# College of Science and Computer Studies

# S-ITCS227LA — Application Development & Emerging Technologies (Laboratory)
# Finals Laboratory Activity No. 2

# Monday, April 22, 2024
# Write a function in python that read lines from file “lyrics.txt” and count how many times the word “Blue” exist in file.  The output of the code should contain the following:
# - Prints the content of the text file using the read method.
# - The Number of time words "Blue" occur.
# - Prints the Title and artist of the lyrics
# Save the python file to “FileHandling_Surname” and include the  screenshot of python output in submission box.

from google.colab import drive
drive.mount('/gdrive')

lyrics_file = open('/gdrive/My Drive/Documents/Reference Documents/BCS2 ITCS227LA/lyrics.txt')
lyrics = lyrics_file.read()
word = "blue"
word_count = 0

print("\n")
print("The lyrics you have inserted are as follows:")
print("==============\n")

print(lyrics)
print("\n==============\n")

lines = lyrics.split("\n")
for line in lines:
  if line.find(word) != -1:
    word_count += 1

print(f'Total word count for "{word}" is: {word_count}')

print("\nINFORMATION ABOUT THIS TRACK —")
print("青のすみか (Where Our Blue Is)")
print("by キタニタツヤ (Tatsuya Kitani)")