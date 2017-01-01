# Koch_Snowflake
This makes a Koch_Snowflake with every component being customizable, even the scaling factor.

To alter all the parameters, you must unfortunately actually edit the main file. I will fix this later.

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
halfSidelets = Boolean (Experimental, only working well for scalingfactor = 1/3) Only includes sidelet 1 at each step.  
Sidelets = Boolean, includes both 1 and 3. This is working just fine! Be warned it significantly increases processing required.  

Note, if the scaling factor is not 1/3rd, the sidelets are of size `(line segment they were placed upon length)*scalingfactor`
This produces slightly asymetrical results due to the order of writing if scaling factor is not 1/3rd. I'm working on fixing this. 
