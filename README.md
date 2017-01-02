# Koch_Snowflake
This makes a Koch Snowflake with every component being customizable, even the scaling factor!  
It currently needs a better color scheme though

To alter all the parameters, edit them in config.py.

A quick description of the parameters:
canvas_size = The size you want the actual image to be, its a square so its just one parameter.  
scalingfactor = the factor you want every successive length to be multiplied by. In the default Koch star its 1/3rd.  
sidelength = The initial side length for the base of the star  
maxdepth = The number of iterations it should go through  
fillcolor = array of colors for each depth  
reversefillcolor = array of colors for each depth, except for when the triangles are reversed.  
outlinecolor = outline color for initial triangle.   
reverse = Boolean for whether you want triangles going inward also.  
bgcolor = Color for the canvas background. It is any color that python supports, so it can be "black" or any hex color like   "#AABBCC"  
```
      __/\__   
      \    /     
__/\__/    \__/\__  
  1     2      3  
```
By sidelets, I am reffering to 1 and 3 in the above diagram, the parts that pop up on the remaining sides  
halfSidelets = Boolean, Only includes sidelet 1 at each step.  
Sidelets = Boolean, includes both 1 and 3. Be warned it significantly increases processing required.  

Note, if the scaling factor is not 1/3rd, the sidelets are of size `(line segment they were placed upon length)*scalingfactor`

thirdtriangleside = Boolean. This is only applicable when Sidelets and reverse are enabled. The parameter specifies whether you want three triangles in each inner triangle or not. Generally speaking, you get more circular looking patterns with it disabled, and more triangle looking patterns when its enabled. See the two sample image 11's  

drawTrianglesAtEnd = Boolean, It saves all triangle writing until the end, and draws it tier by tier instead of my recursive method. This will significantly increase memory usage  

saveEachIteration = Boolean, This is cool if you want to see the progression. Only works with drawTrianglesAtEnd.

