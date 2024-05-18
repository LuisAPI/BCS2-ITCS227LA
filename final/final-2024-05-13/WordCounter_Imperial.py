# De La Salle University – Dasmariñas
# S-ITCS227LA — Application Development & Emerging Technologies (Laboratory)

# Final Exam
# Create a program that reads a text file and counts the frequency of each word in the file.

import collections
from os import system
import re

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\'?\w*\b', text)
        word_count = collections.Counter(words)

    return word_count

try:
    file_path = "D:/Luis/OneDrive - De La Salle University-Dasmariñas/Documents/Academic Documents/BCS2 ITCS227LA/final/final-2024-05-13/Trees.txt"
    word_count = count_words(file_path)

    print('Word Frequencies:')
    print('--------------------------')
    for word, count in word_count.most_common():
        print(f'{word:<15}: {count}')
except:
    print("ERROR:", repr(system.exception()))