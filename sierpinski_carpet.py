#!/usr/bin/env python3

from PIL import Image, ImageFilter, ImageDraw
import numpy
import sys, getopt
from time import gmtime, strftime
import math


def main(argv):

    imgname = "carpet_" + strftime("%m-%d_%H:%M", gmtime())+".jpg"
    canvas_size = 2000
    sides = 3
    sidelength = 600
    bgcolor = "black"
    fillcolor = ["#33DDDD","#55BBCC","#66AACC","#7788BB","#8977AC","#9F66BC","#AA66AA","#CC99CC","#CCDDDD"]
    try:
        opts, args = getopt.getopt(argv,"o:c:",["output=","canvas="])
    except getopt.GetoptError:
        print('sierpinski_carpet.py -o <output image name> -c <canvas size in pixels>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-o", "--output"):
            imgname = arg
        elif opt in ("-c", "--canvas"):
            canvas_size = int(arg)

    img = Image.new("RGBA",(canvas_size,canvas_size),bgcolor)
    c = canvas_size/2 #center
    l = sidelength
    draw = ImageDraw.Draw(img)

    innertheta = 2*math.pi / sides
    if(sides % 2 == 0):
        print('tbc')
    else:
        lengthfromcenter = l / (math.sqrt(2-2*math.cos(innertheta)))
        points = []
        theta = 0
        for i in range(sides):
            points.append( (c + lengthfromcenter*math.cos(theta), c - lengthfromcenter*math.sin(theta)) )
            theta += innertheta

        draw.polygon(points, fillcolor[0])

    if("/" not in imgname):
        imgname = "output/carpet/carpet_"+imgname
    img.save(imgname,"JPEG")




if __name__ == "__main__":
   main(sys.argv[1:])
