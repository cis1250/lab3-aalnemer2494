#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ")








sentence = input("Enter a sentence: ")

while not is_sentence(sentence):
    print("That doesn't look like a valid sentence. Please try again.")
    sentence = input("Enter a sentence: ")


sentence = sentence.lower()


tokens = sentence.split()


punct = ".,!?;:\"'()[]{}"
words = []
for t in tokens:
    w = t.strip(punct)
    if w != "":
        words.append(w)


unique_words = []
frequencies = []

for w in words:
    if w in unique_words:
        idx = unique_words.index(w)
        frequencies[idx] = frequencies[idx] + 1
    else:
        unique_words.append(w)
        frequencies.append(1)


print("Word frequencies:")
for i in range(len(unique_words)):
    print(unique_words[i], ":", frequencies[i])


print("This sentence has", len(words), "words.")
