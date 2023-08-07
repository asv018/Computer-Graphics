import turtle

# Set the background color
turtle.bgcolor("lightgreen")

# Define the functions to draw the hut
def draw_front():
  turtle.forward(100)
  turtle.left(90)
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(100)
  turtle.left(90)
  turtle.forward(50)

def draw_top():
  turtle.up()
  turtle.goto(0, 50)
  turtle.down()
  turtle.right(135)
  turtle.forward(50 * (3 ** 0.5))
  turtle.left(90)
  turtle.forward(50 * (3 ** 0.5))
  turtle.right(135)

def draw_side():
  turtle.up()
  turtle.goto(100, 0)
  turtle.down()
  turtle.right(90)
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(100)
  turtle.left(90)
  turtle.forward(50)

# Draw the hut
draw_front()
draw_top()
draw_side()

# Keep the turtle window open
turtle.done()
