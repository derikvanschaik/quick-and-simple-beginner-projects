# quick-and-simple-beginner-projects
This will be a folder of quick and simple beginner projects I think up of for fun. I am thinking of making a code along series on youtube where I will build these in real time.

### 1. app.js, index.html -- similar to the pysimplegui find and replace app, will find and replace a word you wish to replace from the text you provided in the text area. Features: Clear, copy, find, replace, word count, character count. 

### sums2.py
This visualizes the Reiman sums over the interval of (9,95) for the y = x function. The visualization is fantastic and is what this is really about. I wanted to include the area calculation as well, however the math is a bit off. Obviously as you increase the number of rectangles the area should go from being a poorer estimation to a better one--but this isn't the case with this program. Obviously this isn't really about the math and more about the visualization, I kind of think the issue is with floating point values here but I will come back to it and see if there's any way to remedy this. 
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/sums2.gif)

### sums3.py
Like sums2.py but you can now change the [a,b] intervals by dragging! Isn't that cool. Check it out:
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/sums3.gif)

### sorting.py
Animates insertion sort and selection sort on user provided series (seperated by spaces) or a randomly generated array
of length determined by slider that user slides. Milliseconds of animation (animation speed) are determined in final input on layout.
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/sorting.gif)

### zoom.py
creates 'zoom' feature on pysimplegui graph. 
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/zoom.gif)


### canvasfun.py
Fun Concept of creating and dragging multiple objects onto the graph widget. If you're coding this and would like to make additional enhancements here are a few off the top of my head: 1. Make the dimensions of the objects variable -- perhaps a slider to increase or decrease the size of the circles or the width and height of the rectangles? 2. Draw other objects -- this is made somewhat easier for us due to the 'draw_polygon' method from the graph object. Have fun with it! 
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/canvasfun.gif)

### canvasfun2.py
This is a super fast protype showing how you can make a clicking cursor using the pysimplegui graph element (which I interchangeably call 'Canvas' often. Sorry about that!)
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/canvasfun2.gif)

### animate.py 
Animates the angles of the unit circle, you can control the speed of the animation using the slider widget. Plenty more cool things you can do with this. 
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/animate.gif)

### htmlcanvasfun.html and canvasfun.js 
Testing out the DOM html canvas api. Lots of fun so far. More to come with this as I learn this canvas element more thoroughly! Excited to get more javascript into this particular repo. 
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/canvasfunjs.gif)

###  constrainedinput.py:
This quick project is supposed to simulate a social media bio where there is a maximum amount of characters. Very simple to make yet that does not mean it is not fun or extremely easy either, the coder must still juggle a couple of moving parts... here is a demo:
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/constrainedinputgif.gif)

###  findandreplace.py:
This quick project is supposed to simulate a the find and replace feature we can find in many text apps. For now it really only works when you work on text that you have written in real time, but hey why not make it work for text that you copy and paste from the web! Demo:
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/findandreplace.gif)

###  virtualplotter.py: 
This is a good introduction to the 'graph' object from pysimplegui. Probably my favorite element, especially since it blows the door open on the type of projects you can make with PSG. Go check out my repositories named: 'MIMI' and/or 'mindmap' for different mindmap applications that use this graph element.
This virtual plotter tells you in real time where the current point on the line is, and moves the point up the y=x line if you press 'j' and down if you press 'k'. Try it out. Demo: 
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/virtualplotter.gif)

###  dragging.py:
Did I mention that I love the graph object?? My god is this an amazing feauture, I wish I had discovered it long ago. Anyways, I just figured out one implementation of the 'dragging' objects on the canvas while writing this out. So much fun! I need to add this functionality to my 'MIMI' and 'mindmap' applications. 
Demo:
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/dragging.gif)

###  econpy.py:
Just some more graph fun. Demo:
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/econpy.gif)

###  enhancedplotter.py:
This is a program where you use the user input to plot observations onto the graph. you practice getting user input, creating a plotting graph, plotting the elements and have some fun with the random.randint() function to increase the variability between observations. Fantastic. 
Demo: 
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/enhancedplotter.gif)

###  tangency.py:
This one was so much fun to make, anyone who has taken calculus will surely love this one. This plots the tangency line at the given x point on the y = x^2 curve we have plotted. The beauty of this is that (like all the other projects in this repo) we made this from scratch using only the pysimplegui canvas -- no external plotting library or anything. It shows how much we can do with this module. Check it out! 
Demo: 
![Alt Text](https://github.com/derikvanschaik/quick-and-simple-beginner-projects/blob/main/tangency.gif)

###  surveybuilderdemo.py:
Code along with me and make this survey building application from scratch: https://www.youtube.com/watch?v=f7PnELO1knw

Note: A lot of inspiration is drawn from the PySimpleGUI Demo projects, I will be implementing all these projects with my own ideas and ways of implementation but if the concepts seem eerily familiar that is probably because I have read A LOT of demo projects in my day. The demo programs I speak of can be found here: https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms
