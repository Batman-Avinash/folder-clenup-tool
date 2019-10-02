"""
Created on Wed Oct  2 16:27:03 2019

@author: avinash
"""

import os


dir_content = os.listdir('.')

def find(word, letter):
    index = -1
    while(index < len(word)):
        if word[index] == letter:
            return(index)
        index -= 1
    return -1

def get_files(dir_name):
    list_of_files = []
    list_of_dirs = []
    clean_file_list = []
    for file in dir_name:
        if os.path.isfile(file):
            list_of_files.append(file)
        elif os.path.isdir(file):
            list_of_dirs.append(file)
        else:
            print('Something else')
            
    for file in list_of_files:
        position = find(file, '.')
        cleaned_position = position + 1
        clean_name = file[cleaned_position:]
        clean_file_list.append(clean_name)

get_files(dir_content)
