#!/usr/bin/env python3

from PIL import Image, ImageFilter, ImageDraw
import numpy
import sys, getopt
from time import gmtime, strftime
import math
import config

def main(argv):

    imgname = "output/snowflake_" + strftime("%m-%d_%H:%M", gmtime())

    global canvas_size,scalingfactor,sidelength,maxdepth,reversefillcolor,fillcolor,outlinecolor,bgcolor
    global reverse,sidelets,halfsidelets,thirdtriangleside,sideletsNoDepthIncrease,drawTrianglesAtEnd
    global saveEachIteration, genconfig
    canvas_size = config.canvas_size
    scalingfactor = config.scalingfactor
    sidelength = config.sidelength
    maxdepth = config.maxdepth
    fillcolor = config.fillcolor
    reversefillcolor = config.reversefillcolor
    bgcolor = config.bgcolor
    reverse = config.reverse
    halfsidelets = config.halfsidelets
    sidelets = config.sidelets
    thirdtriangleside = config.thirdtriangleside
    sideletsNoDepthIncrease = config.sideletsNoDepthIncrease
    drawTrianglesAtEnd = config.drawTrianglesAtEnd
    saveEachIteration = config.saveEachIteration
    genconfig = config.genconfig

    if(drawTrianglesAtEnd):
        global trianglelist
        trianglelist = []
    try:
        opts, args = getopt.getopt(argv,"ho:c:",["help","output=","canvas=","scalingfactor=","length=", "depth=","bgcolor=",
        "reverse=","halfsidelets=","sidelets=","threetriangle=","sideletsNoDepthIncrease=","drawTrianglesAtEnd=",
        "saveEachIteration=","genconfig=","fillcolor=","reversefillcolor="])
    except getopt.GetoptError as e:
        print('koch_snowflake.py -o <output image name> -c <canvas size>')
        print(' --[scalingfactor, length, depth, bgcolor, reverse, fillcolor'+
            ' reversefillcolor, halfsidelets, sidelets, threetriangle, sideletsNoDepthIncrease, ' +
            'drawTrianglesAtEnd, saveEachIteration, genconfig]')
        print(e)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-o", "--output"):
            imgname = arg
        elif opt in ("-c", "--canvas"):
            canvas_size = int(arg)
        elif opt in ("-h", "--help"):
            print('koch_snowflake.py -o <output image name> -c <canvas size>')
            print(' --[scalingfactor, length, depth, bgcolor, reverse, fillcolor,'+
                ' reversefillcolor, halfsidelets, sidelets, threetriangle, sideletsNoDepthIncrease, ' +
                'drawTrianglesAtEnd, saveEachIteration, genconfig]')
            return
        elif opt in ("--scalingfactor"):
            scalingfactor = float(arg)
        elif opt in ("--length"):
            sidelength = int(arg)
        elif opt in ("--depth"):
            maxdepth = int(arg)
        elif opt in ("--bgcolor"):
            bgcolor = arg
        elif opt in ("--reverse"):
            reverse = bool(arg)
        elif opt in ("--fillcolor"):
            fillcolor = eval(arg)
        elif opt in ("--reversefillcolor"):
            reversefillcolor = eval(arg)
        elif opt in ("--reverse"):
            reverse = bool(arg)
        elif opt in ("--halfsidelets"):
            halfsidelets = bool(arg)
        elif opt in ("--sidelets"):
            sidelets = bool(arg)
        elif opt in ("--threetriangle"):
            thirdtriangleside = bool(arg)
        elif opt in ("--sideletsNoDepthIncrease"):
            sideletsNoDepthIncrease = bool(arg)
        elif opt in ("--drawTrianglesAtEnd"):
            drawTrianglesAtEnd = bool(arg)
        elif opt in ("--saveEachIteration"):
            saveEachIteration = bool(arg)
        elif opt in ("--genconfig"):
            genconfig = bool(arg)

    if("/" not in imgname):
        imgname = "output/"+imgname

    if(maxdepth > len(fillcolor)):
        for i in range(maxdepth - len(fillcolor)+1):
            fillcolor.append(fillcolor[len(fillcolor)-1])
    if(maxdepth > len(reversefillcolor)):
        for i in range(maxdepth - len(reversefillcolor)+1):
            reversefillcolor.append(reversefillcolor[len(reversefillcolor)-1])

    img = Image.new("RGBA",(canvas_size,canvas_size),bgcolor)
    c = canvas_size/2 #center
    l = sidelength
    draw = ImageDraw.Draw(img)
    triangle = [(c-l/2,c+l/(2*math.sqrt(3)) ),(c,c-l/(math.sqrt(3)) ),(c+l/2,c+l/(2*math.sqrt(3)) )]
    #print(triangle)
    draw.polygon(triangle, fillcolor[0])
    recurse(triangle, l*scalingfactor,1,draw)
    if(drawTrianglesAtEnd and not (not reverse and (sidelets or halfsidelets))):
        print(str(len(trianglelist)+1) + " triangles are in this fractal!!!")
        print("Currently drawing these triangles")
        for i in range(1, maxdepth+1):
            #Fancy way of iterating over a list that allows you to delete elements from it while iterating
            #https://stackoverflow.com/questions/6022764/python-removing-list-element-while-iterating-over-list
            for j in range(len(trianglelist) - 1, -1, -1):
                element = trianglelist[j]
                if(element[0]==i):
                    draw.polygon(element[2],element[1])
                    #no reason to iterate over it again.
                    del trianglelist[j]
            if(saveEachIteration):
                img.save("output/snowflake_"+strftime("%m-%d_%H:%M", gmtime())+"_iter_"+ str(i)+".jpg","JPEG")
    elif(drawTrianglesAtEnd and (not reverse and (sidelets or halfsidelets))):
        print(str(len(trianglelist)+1) + " triangles are in this fractal!!!")
        print("Currently drawing these triangles")
        for i in range(1, maxdepth+1):
            k = maxdepth+1 - i
            #Fancy way of iterating over a list that allows you to delete elements from it while iterating
            #https://stackoverflow.com/questions/6022764/python-removing-list-element-while-iterating-over-list
            for j in range(len(trianglelist) - 1, -1, -1):
                element = trianglelist[j]
                if(element[0]==k):
                    draw.polygon(element[2],element[1])
                    #no reason to iterate over it again.
                    del trianglelist[j]

            if(saveEachIteration):
                img.save(imgname+"_iter_"+ str(i)+".jpg","JPEG")
        draw.polygon(triangle, fillcolor[0])
    img.save(imgname+".jpg","JPEG")
    if(genconfig):
        generateconfig(imgname+".txt")

def recurse(sides,length,curdepth,draw):
    if(sidelets or halfsidelets):
        newsidelist = []
    if(curdepth > maxdepth):
        return
    if(length < .3):
        return

    #this works because its an equilateral triangle
    xcenter = (sides[0][0]+sides[1][0]+sides[2][0])/3
    ycenter = (sides[0][1]+sides[1][1]+sides[2][1])/3
    #iterate through each pair of sides
    for i in range(3):
        p1 = sides[i]
        for j in range(i+1,3):
            drawthisiter = True
            #ignore this side as it would be going into triangle, unless it needs to be accounted for sidelets.
            if(i+j == 1 and curdepth > 1 and not sidelets):
                continue
            elif(i+j == 1 and curdepth > 1 and sidelets and not thirdtriangleside):
                drawthisiter = False
            p2 = sides[j]

            #midpoints
            xmid = (p1[0] + p2[0])/2
            ymid = (p1[1] + p2[1])/2

            #slope, rise over run
            m = (p2[1]-p1[1]) / (p2[0]-p1[0])
            # total side length / 2 * (length on line per unit x), since its per unit x, dx will be the total
            #change in x from midpoint. /2 is b/c midpoint
            dx = length / (2*math.sqrt(m*m + 1))
            dy = m*dx
            newp1 = (xmid - dx, ymid - dy)
            newp2 = (xmid + dx, ymid + dy)

            #sqrt 3 scales length to new perpendicular's length. negative is because its
            #perp, and therefore direction is reversed
            if(m != 0):
                dx = length * math.sqrt(3)/(2*math.sqrt(1 + (1/(m*m))))
                dy = dx/m

                if(xmid < xcenter and dx > 0):
                    dx *= -1
                elif(xmid > xcenter and dx < 0):
                    dx *= -1
                if(ymid < ycenter and dy > 0):
                    dy *= -1
                elif(ymid > ycenter and dy < 0):
                    dy *= -1

            else:
                dx = 0
                dy = length*math.sqrt(3)/2
                if(ymid < ycenter and dy > 0):
                    dy *= -1
            newp3 = (xmid+dx,ymid+dy)
            newsides = [newp1, newp2, newp3]
            if(halfsidelets or sidelets):
                newsidelist.append(newsides[:-1])
            #print(str(newsides))

            if(drawthisiter):
                if(not drawTrianglesAtEnd):
                    draw.polygon(newsides, fillcolor[curdepth])
                else:
                    trianglelist.append((curdepth,fillcolor[curdepth],newsides))

            recurse(newsides,length*scalingfactor,curdepth+1,draw)
            if(reverse):
                newp3 = (xmid-dx,ymid-dy)
                newsides = [newp1, newp2, newp3]
                #print(str(newsides))

                if(drawthisiter):
                    if(not drawTrianglesAtEnd):
                        draw.polygon(newsides, reversefillcolor[curdepth])
                    else:
                        trianglelist.append((curdepth,reversefillcolor[curdepth],newsides))

                recurse(newsides,length*scalingfactor,curdepth+1,draw)
    if(halfsidelets or sidelets):
        if(curdepth == maxdepth):
            return
        for i in range(len(newsidelist)):
            nside1 = newsidelist[i]

            #iterate through each pair of new sides. New side refers to sides generated previously in this recurse
            for j in range(i+1,len(newsidelist)):
                nside2 = newsidelist[j]

                #p1 means nside1_point_1, p2 means nside1_point_2, p3 means nside2_point_1, p4 means nside2_point_2
                #distance squared, because theres no reason to do the time-intense square root
                distSqrp1p3 = distSqrd(nside1[0],nside2[0])
                distSqrp1p4 = distSqrd(nside1[0],nside2[1])
                distSqrp2p3 = distSqrd(nside1[1],nside2[0])
                distSqrp2p4 = distSqrd(nside1[1],nside2[1])
                mindist = min(distSqrp1p3,distSqrp1p4,distSqrp2p3,distSqrp2p4)

                points = 0
                if(mindist == distSqrp1p3):
                    points = [nside1[0],nside2[0]]
                elif(mindist == distSqrp1p4):
                    points = [nside1[0],nside2[1]]
                elif(mindist == distSqrp2p3):
                    points = [nside1[1],nside2[0]]
                elif(mindist == distSqrp2p4):
                    points = [nside1[1],nside2[1]]
                #now given these points, I need to find closest point in sides
                #since they are all equidistant, I only need to find the closest point in sides
                #to a single point in points
                dists = [0,0,0]
                for h in range(3):
                    dists[h] = distSqrd(sides[h], points[0])

                mindist = min(dists)
                for h in range(3):
                    if(mindist == dists[h]):
                        points.append(sides[h])


                #print("points " + str(points))
                #print("-------------------------------------")
                if(sideletsNoDepthIncrease):
                    recurse(points,math.sqrt(mindist)*scalingfactor,curdepth,draw)
                else:
                    recurse(points,math.sqrt(mindist)*scalingfactor,curdepth+1,draw)

#distance squared, because theres no reason to do the time-intense square root
def distSqrd(p1,p2):
    return (  ((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)  )

def generateconfig(filename):
    configcopy = open(filename, "w+")
    configcopy.write("canvas_size = " + str(canvas_size)+"\n")
    configcopy.write("scalingfactor = " + str(scalingfactor)+"\n")
    configcopy.write("sidelength = " + str(sidelength)+"\n")
    configcopy.write("maxdepth = " + str(maxdepth)+"\n")
    configcopy.write("fillcolor = " + str(fillcolor)+"\n")
    configcopy.write("reversefillcolor = " + str(reversefillcolor)+"\n")
    configcopy.write("bgcolor = " + str(bgcolor)+"\n")
    configcopy.write("reverse = " + str(reverse)+"\n")
    configcopy.write("halfsidelets = " + str(halfsidelets)+"\n")
    configcopy.write("sidelets = " + str(sidelets)+"\n")
    configcopy.write("thirdtriangleside = " + str(thirdtriangleside)+"\n")
    configcopy.write("sideletsNoDepthIncrease = " + str(sideletsNoDepthIncrease)+"\n")
    configcopy.write("drawTrianglesAtEnd = " + str(drawTrianglesAtEnd)+"\n")
    configcopy.write("saveEachIteration = " + str(saveEachIteration)+"\n")
    configcopy.write("genconfig = " + str(genconfig)+"\n")
    configcopy.write(("\npython3 koch_snowflake.py -c {} --scalingfactor={} --length={}"+
    " --depth={} --fillcolor=\"{}\" --reversefillcolor=\"{}\" --bgcolor=\'{}\'" +
    " --reverse={} --halfsidelets={} --sidelets={} --threetriangle={} --sideletsNoDepthIncrease={}"+
    " --drawTrianglesAtEnd={}  --saveEachIteration={}  --genconfig={} ").format(canvas_size,scalingfactor,
    sidelength,maxdepth,fillcolor,reversefillcolor,bgcolor, reverse,halfsidelets,
    sidelets, thirdtriangleside, sideletsNoDepthIncrease, drawTrianglesAtEnd, saveEachIteration,
    genconfig) )
    configcopy.close()


if __name__ == "__main__":
   main(sys.argv[1:])
