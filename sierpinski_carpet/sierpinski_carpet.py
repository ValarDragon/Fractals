#!/usr/bin/env python3

from PIL import Image, ImageFilter, ImageDraw
import numpy
import sys, getopt
from time import gmtime, strftime
import math
import config

def main(argv):

    global sides,fillcolor,iterations,scalingfactor,numonline,innertheta,canvas_size,innerlengthconstant
    global rotSides,bgcolor,genconfig,generateCornerPolygons,rotateCornerPolygons,cornerPolygonElongSidelength
    canvas_size = config.canvas_size
    sides = config.number_of_sides
    sidelength = config.sidelength
    iterations = config.iterations
    scalingfactor = config.scalingfactor
    numonline = 1
    rotSides = config.rotSides
    generateCornerPolygons = config.generateCornerPolygons
    rotateCornerPolygons = config.rotateCornerPolygons
    cornerPolygonElongSidelength = config.cornerPolygonElongSidelength
    #Not global, intentional.
    m2cdist = config.midpoint2centerDistance

    imgname = ""
    bgcolor = config.bgcolor
    fillcolor = config.fillcolor
    genconfig = config.genconfig

    try:
        opts, args = getopt.getopt(argv,"s:o:c:",["sides=","output=","canvas="])
    except getopt.GetoptError:
        print('sierpinski_carpet.py -o <output image name> -c <canvas size in pixels>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-o", "--output"):
            imgname = arg
        elif opt in ("-c", "--canvas"):
            canvas_size = int(arg)
        elif opt in ("-s", "--sides"):
            sides = int(arg)

    imgname = "output/carpet_" + str(sides) + "_" + strftime("%m-%d_%H:%M", gmtime())

    img = Image.new("RGBA",(canvas_size,canvas_size),bgcolor)
    c = canvas_size/2 #center
    sidelength
    draw = ImageDraw.Draw(img)

    innertheta = 2*math.pi / sides
    theta = 0
    if(sides % 2 == 0):
        theta = math.pi/2 - (innertheta/2)
    else:
        theta = math.pi/2

    innerlengthconstant = math.sqrt(2-2*math.cos(innertheta))
    lengthfromcenter = sidelength / innerlengthconstant
    points = polygonCorners((c,c),lengthfromcenter,theta)

    draw.polygon(points, fillcolor[0])
    #print("center: " + str(c))
    recurse(points,theta,sidelength*scalingfactor,(c,c),1,m2cdist,draw)

    if("/" not in imgname):
        imgname = "output/"+imgname
    img.save(imgname+".jpg","JPEG")
    if(genconfig):
        generateconfig(imgname+".txt",m2cdist,sidelength)

def recurse(points,theta0point,newlength,center,curdepth,m2cdist,draw):
    if(curdepth > iterations):
        return
    #loop through each side
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i+1)%sides]
        midpoint = ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
        #print("midpoint: " + str(midpoint))
        #center to midpoint is the slope that is perpendicular to the side
        #slope = (p2[1]-p1[1])/(p2[0]-p1[0])
        #draw.line((center,midpoint),"red")

        theta = math.atan2(midpoint[1]-center[1],midpoint[0]-center[0])
        if(theta < 0):
            theta += 2*math.pi
        newcenter = (midpoint[0] + m2cdist*math.cos(theta), midpoint[1] + m2cdist*math.sin(theta))

        lengthfromcenter = newlength / innerlengthconstant

        if(rotSides):
            if(sides % 2 == 0):
                theta += innertheta/2
            else:
                theta += math.pi

        newpoints = polygonCorners(newcenter,lengthfromcenter,theta)

        draw.polygon(newpoints, fillcolor[curdepth])
        recurse(newpoints,theta,newlength*scalingfactor,newcenter,curdepth+1,m2cdist*scalingfactor,draw)

        if(generateCornerPolygons == True):
            theta = math.atan2(p1[1]-center[1],p1[0]-center[0])
            newcenter = (0,0)
            if(theta < 0):
                theta += 2*math.pi
            if(cornerPolygonElongSidelength == 0):
                newcenter = (p1[0] + m2cdist*math.cos(theta), p1[1] + m2cdist*math.sin(theta))
            elif(cornerPolygonElongSidelength == 1):
                newcenter = (p1[0] + math.sqrt(2)*m2cdist*math.cos(theta), p1[1] + math.sqrt(2)*m2cdist*math.sin(theta))
            elif(cornerPolygonElongSidelength == 2):
                #do it this way to avoid division by zero errors
                sinSign = 0
                try:
                    sinSign = abs(math.sin(theta)) / math.sin(theta)
                except Exception:
                    pass
                cosSign = 0
                try:
                    cosSign = abs(math.cos(theta)) / math.cos(theta)
                except Exception:
                    pass
                newcenter = (p1[0] + m2cdist*cosSign, p1[1] + m2cdist*sinSign)

            lengthfromcenter = newlength / innerlengthconstant

            if(rotSides and not rotateCornerPolygons):
                if(sides % 2 == 0):
                    theta += innertheta/2
                else:
                    theta += math.pi

            newpoints = polygonCorners(newcenter,lengthfromcenter,theta)
            draw.polygon(newpoints, fillcolor[curdepth])
            recurse(newpoints,theta,newlength*scalingfactor,newcenter,curdepth+1,m2cdist*scalingfactor,draw)

def polygonCorners(center, lengthfromcenter, theta0):
    corners = []
    for j in range(sides):
        corners.append( (center[0] + lengthfromcenter*math.cos(theta0), center[1] - lengthfromcenter*math.sin(theta0)))
        theta0 += innertheta
    return corners

def generateconfig(filename,m2cdist,sidelength):
    configcopy = open(filename, "w+")
    configcopy.write("canvas_size = " + str(config.canvas_size)+"\n")
    configcopy.write("number_of_sides = " + str(sides)+"\n")
    configcopy.write("rotSides = " + str(rotSides)+"\n")
    configcopy.write("scalingfactor = " + str(scalingfactor)+"\n")
    configcopy.write("sidelength = " + str(sidelength)+"\n")
    configcopy.write("iterations = " + str(iterations)+"\n")
    configcopy.write("midpoint2centerDistance = " + str(m2cdist)+"\n")
    configcopy.write("fillcolor = " + str(fillcolor)+"\n")
    configcopy.write("bgcolor = \"" + str(bgcolor)+"\"\n")
    configcopy.write("genconfig = " + str(genconfig)+"\n")
    configcopy.write("generateCornerPolygons = " + str(generateCornerPolygons)+"\n")
    configcopy.write("rotateCornerPolygons = " + str(rotateCornerPolygons)+"\n")
    configcopy.write("cornerPolygonElongSidelength = " + str(cornerPolygonElongSidelength)+"\n")
    configcopy.close()

if __name__ == "__main__":
   main(sys.argv[1:])
