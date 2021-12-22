import turtle

scr = turtle.Screen()
scr.bgcolor("orange")
turtle.shape("turtle")

# for i in range(0, 10):
#     turtle.right(36)
#     for i in range(0, 5):
#         turtle.forward(100)
#         turtle.right(72)

for x in range(0,10):
    for i in range(0,8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)


turtle.exitonclick()