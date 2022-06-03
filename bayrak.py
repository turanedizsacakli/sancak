import turtle

t=turtle.Turtle()
w=turtle.Screen()
w.setup(width=720, height=420)
w.bgcolor("red")

t.up()
t.goto(-100,-100)
t.color("white")
t.begin_fill()
t.circle(120)
t.end_fill()

t.goto(-70,-80)
t.color("red")
t.begin_fill()
t.circle(100)
t.end_fill()

t.goto(0,35)
t.fillcolor("white")
t.begin_fill()

for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

t.goto(-60,-190)
t.color("white")
t.write("turan ediz saçaklı", font=("Verdana",7,"bold"))

t.goto(-999,-0)

w.exitonclick()
