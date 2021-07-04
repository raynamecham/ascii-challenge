from ascii_canvas import canvas
from ascii_canvas import item

canvas_ = canvas.Canvas()

shape = item.Item('+-----------+\n|           |\n+-----------+', position=[0, 0])
shape2 = item.Item('+-----------+\n|           |\n+-----------+', position=[5, 1])


canvas_.add_item(shape)
canvas_.add_item(shape2)

print(canvas_.render())
