import turtle

#set up the screen
wn = turtle.Screen()
wn.pos()
wn.title("snake game")
wn.bgcolor("Blue")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 50)
head.direction = "stop"
turtle.mainloop()





