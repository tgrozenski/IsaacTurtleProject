import random
import turtle

def trippy_stairs():

    tina = turtle.Turtle()
    tina.width(5)
    tina.up()
    tina.goto(-300, 300)
    tina.down()

    for i in range(30):
        distance = random.randint(20, 50) # Choose a random number between 20-50
        tina.forward(distance)

        tina.right(90)
        
        tina.forward(distance)
        
        tina.left(90)

    turtle.done()

def make_art() -> None:
    """
    Uses two or more random variables
    Uses loops instead or repeating code
    Two or more uses of for loops or while loops
    Two or more uses of if statements
    Choose either bkgrd image, user input, or new function
    Big Add On: either layer elements, cool math, random innovation or functions
    Make it interesting 
    """
    tina = turtle.Turtle()
    tina.speed(8) # set the speed of the pen

    # get number of circles and validate it 
    num_circles = 100
    while num_circles > 5:
        user_input = input('Enter a number of circles to draw less than 5 : ')
        num_circles = int(user_input)
    
    # add a layer element here

    color_list = ['red', 'green', 'blue', 'purple', 'orange', 'pink']    

    for _ in range(num_circles):

        # setting a random color from the color list
        tina.color(color_list[random.randint(0,len(color_list) - 1)])

        # move to random position without drawing
        tina.penup()
        tina.setx(random.randint(-200,200))
        tina.sety(random.randint(-200,200))
        tina.pendown()

        # draw circle and fill it
        tina.begin_fill()
        tina.circle(random.randint(20, 300))
        tina.end_fill()

    print('user entered', user_input)

if __name__ == '__main__':
    make_art()