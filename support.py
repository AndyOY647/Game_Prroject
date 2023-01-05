from csv import  reader
from os import walk
import pygame
import re


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    # Need a list to store the images and return it
    surface_list = []
    img_numlist = []
    counter = 0

    # The data contains 3 folders and we only care about the last one because it's the one that contains the images
    for _,__,image_files in walk(path):
        for image in image_files:
            for full_path in image:
                img = image.split('_')
                img_two = img[2].split('.')
                #append the img num to the list
            img_num = int(img_two[0])
            img_numlist.append(img_num)
        num_sorted = sorted(img_numlist)
        for i in num_sorted:
           full_path = f'images/other/Other_Tiles_{i}.png'
           print(full_path)
           image_surf = pygame.image.load(full_path).convert_alpha()
           surface_list.append(image_surf)

    return surface_list

#  An example for idea of sorting
# import re
#  def atoi(text):
#     return int(text) if text.isdigit() elsetext
# def natural_keys(text):
#     return [ atoi(c) for c in re.split('(\d+)',text) ]
#  my_list =['Hello1', 'Hello12', 'Hello29', 'Hello2', 'Hello17', 'Hello25']
#  my_list.sort(key=natural_keys)
# print my_list


