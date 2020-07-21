#! /usr/bin/env python
# encoding:utf-8

# This program is main program to convert image format,
# from 'jpg' to 'tiff'.

# usage : python3 this_program image_files.jpg

from PIL import Image
import sys
import os
import shutil

def convertFile(input_file):
    output = str(input_file).split('.')[0] + '.tiff'
    im = Image.open(input_file)
    im.save(output)

    return output

if __name__ == '__main__':
    infiles = sys.argv[1:]
    out_dir = './tiff_files'

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    for i in range(len(infiles)):
        out_file = convertFile(infiles[i])
        shutil.move(out_file, out_dir)
