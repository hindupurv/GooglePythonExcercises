#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class
"""

import sys

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def word_count_dict(filename):
    inputFile = open(filename,'r')
    # convert to lower
    wordCountDict = {}
    for line in inputFile:
        inputWords = line.split() #default is space
        for word in inputWords:
            word = word.lower()
            # use dict for counting
            if not word in wordCountDict.keys():
                wordCountDict[word] = 1
            else:
                wordCountDict[word] = wordCountDict[word] + 1
    inputFile.close()
    return wordCountDict

def print_words(filename):
    word_count = word_count_dict(filename)
    words = sorted(word_count.keys())
    for word in words:
        print(word, word_count[word])

def print_top(filename):
    word_count = word_count_dict(filename)
    def values_of_dict(x):
        return x[1]
    print({k:v for k,v in sorted(word_count.items(), key=values_of_dict, reverse=True)})
    # print({k:v for k,v in sorted(word_count.items(), key=(lambda x: x[1]), reverse=True)})


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    filename ='D:/GooglePythonExercises/basic/alice.txt'
    word_count = word_count_dict(filename)
    #print(word_count)
    #print_words(filename)
    print_top(filename)

if __name__ == '__main__':
  main()
