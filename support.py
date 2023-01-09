from csv import  reader
from os import walk
import pygame

map = {}

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    surface_list = {}

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image

            img_num = image.split("_")[-1].split(".")[0]
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list[img_num] = image_surf
    return surface_list



# def convert(path):
#     import_folder(path)
#     img_numlist =[]
#     for _, __, image_files in walk(path):
#         for image in image_files:
#             for full_path in image:
#                 img = image.split('_')
#                 img_two = img[2].split('.')
#             # print(img_two)
#             # append the img num to the list
#             img_num = int(img_two[0])
#             img_numlist.append(img_num)
#         num_sorted = sorted(img_numlist)
#         # print(num_sorted)
#     return img_numlist

# convert('images/tree')