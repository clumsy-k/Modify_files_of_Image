#! /usr/bin/env python
# encoding:utf-8

# This program is test program to convert from '.jpg' to '*.tiff'.
# usage : python3 this_program.py image.jpg

from PIL import Image
import sys

def convertFile(input_file):
    output = str(input_File).split('.')[0] + '.tiff'
    im = Image.open(input_file)
    im.save(output)

if __name__ == '__main__':
    infile = sys.argv[1]
    convertFile(infile)
