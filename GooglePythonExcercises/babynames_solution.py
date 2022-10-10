#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import glob as gb
import os


def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  inputFile = open(filename,'r', newline='').read()
  list_of_names = []
  #head_20 = str([next(inputFile) for i in range(40,100)])
  #print(head_20)
  year_here = re.search(r'(Popularity)\s(in)\s(\d\d\d\d)', inputFile)
  #print(year_here) #<re.Match object; span=(2340, 2358), match='Popularity in 2006'>
  print("year: ",year_here.group(3))
  
  #tuple = (rank, boy-name, girl-name)
  tuple_data = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', inputFile)
  
  names_rank_dict = {}
  # unpack using for loop the tuple into a dict - name, rank
  for rank, boy_name, girl_name in tuple_data:
      names_rank_dict[boy_name] = rank
      names_rank_dict[girl_name] = rank
  sorted_names = sorted(names_rank_dict.keys())
  for name in sorted_names:
      list_of_names.append(name+" "+names_rank_dict[name])
  return list_of_names    


def main():
  os.chdir('D:/GooglePythonExercises/babynames')
  data_list = []
  for file in gb.glob("*.html"):
      data_list = extract_names(file) 
      print("filename: ",file)
      for names_rank in data_list:
          print(names_rank)
    

  
if __name__ == '__main__':
  main()
