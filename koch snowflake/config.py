#NOTE all True/False's must have the T and F capitalized
#The size of the background. Its a square so you only need a single number, in pixels
canvas_size = 1500
#The factor by which each sucessive generation should shrink by. If you are using scaling factor less than 1/3
#then you should make sure your reversefillcolor and regular fillcolor are the same, otherwhise it will look super weird
#as there will be asymettric overlaps because of the order they are drawn at each level. Same color for each level
#between fill and reverse fill will fix this.
scalingfactor = 1/3
#The length of each side of the initial triangle
sidelength = 900
#The number of iterations
maxdepth = 3

#the color each depth of triangle should have. You make it different for regular ones vs reverse ones
#its an array so feel free to add /remove elements. It takes all valid python colors, so you can add transparencies if
#you are feeling fancy. If you want them to be equal, just make reversefillcolor = fillcolor
fillcolor = ["#33DDDD","#55BBCC","#66AACC","#7777BB","#8977AC","#9F66BC","#AA66AA","#CC99CC","#CCDDDD"]
reversefillcolor = ["#DDDD33","#CCBB55","#CCAA66","#BB7766","#AC7778","#BC668F","#AA66AA","#CC99CC","#CCDDDD"]

#color of the background
bgcolor = "black"
#Do you want triangles going inwards AND outwards? (True for yes, False for no.)
reverse = True

#```
#       __/\__
#       \    /
# __/\__/    \__/\__
#   1     2      3

#By sidelets, I am reffering to 1 and 3 in the above diagram, the parts that pop up on the remaining sides
#NO SIDELETS WILL BE CREATED UNLESS YOU TURN halfsidelets or sidelets on.
#Note, if the scaling factor is not 1/3rd, the sidelets are of size `(line segment they were placed upon length)*scalingfactor`
#halfSidelets = True or False . Makes sidelet '1's get created.
#Sidelets = True or False, makes both sidelet's 1 and 3. Be warned this significantly increases processing required.
halfsidelets = False
sidelets = True

#Works well at depth = 3, not so well at higher depths. Significantly increases processing time.
#It makes sidelets spawn with no increase in their depth. See sample output 13 for what it looks like
sideletsNoDepthIncrease = False

# thirdtriangleside = True or False. This only matters when Sidelets and reverse are both enabled.
# The parameter specifies whether you want three triangles in each inner triangle or not.
# Generally speaking, you get more circular looking patterns with it disabled,
# and more triangle looking patterns when its enabled. See the two sample image 11's.
# NOTE If you want the circular pattern, drawTrianglesAtEnd must be False
thirdtriangleside = True

#This saves all triangle writing until the end, and draws it tier by tier instead of my recursive method.
#This is ONLY important if you have reverse on AND the scaling factor is < 1/3 (The spawned triangles are bigger than normal)
#This will increase memory usage significantly.
drawTrianglesAtEnd = True
#This is cool if you want to see the progression. Only works with drawTrianglesAtEnd.
saveEachIteration = False

#generates a text configuration file, for what settings you used.
genconfig = False
