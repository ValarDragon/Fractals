#NOTE all True/False's must have the T and F capitalized
#The size of the background. Its a square so you only need a single number, in pixels
canvas_size = 2000
#the number of sides. NUMBER ONE THING YOU SHOULD CHANGE!
number_of_sides = 3
#orient sides so that flat side is parallel to offshooting side. Change this setting!!!
rotSides = True
#The factor by which each sucessive polygon, and distance from midpoint to next center scales by.
scalingfactor = 1/3
#The length of each side of the initial polygon
sidelength = 600
#The number of iterations
iterations = 5
#Distance between midpoint of each side of polygon, and center of next polygon. Scales by scaling factor.
midpoint2centerDistance = 300
generateCornerPolygons = False

#the color each depth of polygon should have. Its an array so feel free to add /remove elements.
# It takes all valid python colors, so you can add transparencies if you are feeling fancy.
fillcolor = ["#33DDDD","#55BBCC","#66AACC","#7777BB","#8977AC","#9F66BC","#AA66AA","#CC99CC","#CCDDDD"]

#color of the canvas
bgcolor = "black"

#generates a text configuration file, for what settings you used.
genconfig = False
