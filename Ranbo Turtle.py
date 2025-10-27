#Turtle Lecture Practice
# Import the turtle module
import turtle
import random

# Constants (you can change these)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 450
WINDOW_TITLE = "My First Turtle Program"

# Set up the screen object
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)

# Create the turtle object
t = turtle.Turtle()

## Start of your code

def triangle():
    angle=random.randint(1,360)
    side=random.randint(1,300)
    t.fillcolor('red')
    t.begin_fill()
    t.left(angle)
    for i in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()

def penta():
    screen.numinput("Config","x value")
    screen.numinput("Config","y value")
    
    t.fillcolor(random.random(),random.random(),random.random())

    t.begin_fill()
    for i in range(5):
        t.forward(50)
        t.left(72)
    t.end_fill()

def rainbowS():
    t.hideturtle()
    screen.tracer(False)
    t.speed(0)
    t.pensize(1)
    for i in range(0,100):
        for j in range(0,100):
            t.pencolor(j/100,0,i/100)
            t.forward(1)
        t.up()
        t.right(90)
        t.forward(1)
        t.left(90)
        t.backward(100)
        t.down()
    screen.update()

def stupidcheck(vect):
    for i in vect:
        if i>1:
            vect[vect.index(i)]=1
    return(vect)

def ilovemylife(y,x,ymax,xmax):
    if x//(xmax/6)==0:
        return(stupidcheck([1*(y)/100,(x/100*(y)/100+((y//100)*(y-100)/100)),((y//100)*(y-100)/100)]))
    elif x//(xmax/6)==1:
        return(stupidcheck([(1-(x-100)/100)*y/100+((y//100)*(y-100)/100),1*y/100,((y//100)*(y-100)/100)]))
    elif x//(xmax/6)==2:
        return(stupidcheck([((y//100)*(y-100)/100),1*y/100,(x-200)/100*y/100+((y//100)*(y-100)/100)]))
    elif x//(xmax/6)==3:
        return(stupidcheck([((y//100)*(y-100)/100),(1-(x-300)/100)*y/100+((y//100)*(y-100)/100),1*y/100]))
    elif x//(xmax/6)==4:
        return(stupidcheck([(x-400)/100*y/100+((y//100)*(y-100)/100),((y//100)*(y-100)/100),1*y/100]))
    elif x//(xmax/6)==5:
        return(stupidcheck([(1*y/100),((y//100)*(y-100)/100),(1-(x-500)/100)*y/100+((y//100)*(y-100)/100)]))
    
def sadgrad():
    t.hideturtle()
    screen.tracer(False)
    t.speed(0)
    t.pensize(1)
    for i in range(0,200):
        for j in range(0, 600):
            x=ilovemylife(i,j,200,600)
            t.pencolor(x)
            t.forward(1)
        t.up()
        t.right(90)
        t.forward(1)
        t.left(90)
        t.backward(600)
        t.down()
    screen.update()

def fullgrad():
    t.hideturtle()
    screen.tracer(False)
    t.speed(0)
    t.pensize(1)
    for i in range(0,100):
        for j in range(0, 500):
            t.pencolor(i/100,i/100,i/100)
            t.forward(1)
        t.up()
        t.right(90)
        t.forward(1)
        t.left(90)
        t.backward(500)
        t.down()
    screen.update()

def test():
    t.speed(5)
    t.pensize(15)
    t.forward(300)

#triangle()
#penta()
#rainbowS()
#fullgrad()
sadgrad()

## End of your code

# Make a clean exit
screen.exitonclick()
