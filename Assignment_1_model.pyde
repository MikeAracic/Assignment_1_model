my_colors = [color(240,18,5),color(100,240,200)]
which_color = 0

def setup():
    size(400,400)
    background(0)
    
    
def draw():
    global which_color
    fill(my_colors[which_color % 2])
    circle(200,200,125)
    delay(3000)
    which_color += 1
