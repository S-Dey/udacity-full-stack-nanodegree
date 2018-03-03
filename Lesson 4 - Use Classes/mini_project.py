import turtle

def draw_rhombus(some_turtle):
    for i in range(1, 3):
        some_turtle.forward(100)
        some_turtle.left(45)
        some_turtle.forward(100)
        some_turtle.left(135)

def draw_line(some_line):
    for i in range(1, 2):
        some_line.right(90)
        some_line.forward(300)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("orange")
    
    rhombus = turtle.Turtle()
    rhombus.shape("turtle")
    rhombus.color("green")
    rhombus.speed(1)
    for i in range(1, 37):
        draw_rhombus(rhombus)
        rhombus.right(10)
        #Create the turtle line
        for i in range(37, 38):
            draw_line(rhombus)
    
    window.exitonclick() 

draw_art()