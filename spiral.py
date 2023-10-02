import turtle

wn = turtle.Screen()
wn.bgcolor("white")


pen = turtle.Turtle()
pen.speed(0)  

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(360):
    pen.pencolor(colors[i % 6])  
    pen.forward(i)
    pen.right(59)
    
wn.exitonclick()
