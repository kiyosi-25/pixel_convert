# coding: utf-8
from PIL import Image
import os
import numpy as np
import csv


def cnv_pixel(file_path):
    try:
        im = np.array(Image.open('pict/' + file_path))
        name, ext = os.path.splitext(file_path)
        f = open('csv/' + name + '.csv', 'w')
        writer = csv.writer(f, lineterminator='\n')

        for x in range(im.shape[1]):
            pixel_list = []
            for y in range(im.shape[0]):
                txt = str(im[x, y][0]) + "," + str(im[x, y][1]) + "," + str(im[x, y][2])
                # print('[' + str(x) + ',' + str(y) + ']')
                pixel_list.append(txt)
            writer.writerow(pixel_list)

        f.close()
    except IndexError:
        print(file_path + ':index error')


path = 'pict'

for file in os.listdir(path):
    if not file.startswith('.'):
        print(file)
        cnv_pixel(file)
