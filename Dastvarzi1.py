# Main idea and code get from "https://www.geeksforgeeks.org/how-to-make-indian-flag-using-turtle-python/"
from turtle import *

speed(0)

# configure starting point
penup()
goto(-400, 250)
pendown()

# green Rectangle
color("ForestGreen")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()
left(90)
forward(167)

# red Rectangle
color("#db0000")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

# Allah logo at the center
color("#db0000")
ht()
penup()
goto(-35, -50)
pendown()
write("الله", font=("B Titr", 45, "normal"))

# to hold the output window
done()
