#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:27:03 2019

@author: avinash
"""
import os


# list of files and directory
dir_content = os.listdir('.')


def find(word, letter):
    index = -1
    while(index < len(word)):
        if word[index] == letter:
            return(index)
        index -= 1
    return -1

def remove_duplicate(list_with_duplicate):
    clean_list = []
    for item in list_with_duplicate:
        if item not in clean_list:
            clean_list.append(item)
    return clean_list

def get_folders(dir_name):
    all_folders = []
    for folder in dir_name:
        if os.path.isdir(folder):
            all_folders.append(folder)
        else:
            pass
    return all_folders

def get_files(dir_name):
    all_files = []
    for file in dir_name:
        if os.path.isfile(file):
            all_files.append(file)
        else:
            pass
    return all_files

def folders_to_create(list_of_files, list_of_folders, letter):
    create_list = []
    for file in list_of_files:
        position = find(file, letter)
        cleaned_position = position + 1
        clean_name = file[cleaned_position:]
        create_list.append(clean_name)
    clean_create_list = remove_duplicate(create_list)
    return clean_create_list

def create_folders(list_of_folder_name):
    existing_folders = get_folders(dir_content)
    required_folders = folders_to_create(get_files(dir_content), get_folders(dir_content), letter='.')
    clean_required_folders = []
    
    for item in required_folders:
        if item not in existing_folders:
            clean_required_folders.append(item)
        else:
            pass
    
    if clean_required_folders:
        for folder in clean_required_folders:
            print('Creating Folder: {}'.format(folder))
            os.mkdir(folder)
    else:
        print('Nothing to do')
            
def move_one_file(file_name):
    index = find(file_name, '.') + 1
    folder_to_move = file_name[index:]
    print('Moving {} to {}'.format(file_name, folder_to_move))
    os.rename(file_name, folder_to_move + '/' + file_name)
    
def move_all_files(dir_name):
    all_files = get_files(dir_content)
    
    for file in all_files:
        move_one_file(file)
        
