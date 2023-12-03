from turtle import Turtle,Screen
import turtle as t
import threading
import random

timmy = Turtle()
timmy.shape("turtle")
t.colormode(255)

#for i in range(4):
#    timmy.forward(100)
#    timmy.left(90)

"""for i in range(10):
	timmy.forward(10)
	timmy.pu()
	timmy.forward(10)
	timmy.pd()"""

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angle = [0,90,180,270]
"""for i in range (3,11):
	for j in range(i):
		
		angle = 360/i
		timmy.forward(100)
		timmy.left(angle)
	timmy.color(random.choice(colours))"""


def random_color():
	r = random.randint(1,255)
	g = random.randint(1,255)
	b = random.randint(1,255)
	tup = (r,b,g)
	return tup

"""for i in range(100):
	timmy.forward(50)
	timmy.left(random.choice(angle))
	timmy.pencolor(random_color())"""

"""for i in range(360):
	timmy.circle(200)
	timmy.left(5)
	timmy.setheading(timmy.heading()+10)"""

import colorgram

colors = colorgram.extract('images.jpeg', 6)

first_rgb = colors[0].rgb


















screen = Screen()
screen.exitonclick()