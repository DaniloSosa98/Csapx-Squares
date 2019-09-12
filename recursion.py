import turtle
import math
PEN_WIDTH = 1
MARGIN = 20

def init( size: int, speed: int ):
    """
    The following initialization steps create a square
    window that uses most of the screen, regardless
    of the resolution of the display it runs on.  This
    avoids any trouble with sizing the window.

    :param size: a resolution parameter so that
                 the coordinate system ranges from -20 to size+20 in both dimensions.
    :param speed: a number between 1 and 10 indicating turtle movement speed
                  0 => don't show animation; just draw
    :post: turtle is at 0,0, facing east (0 degrees), pen up
    """

    turtle.reset()
    smaller_dim = min( turtle.window_height(), turtle.window_width() )
    turtle.setup( smaller_dim, smaller_dim )
    turtle.setworldcoordinates( -MARGIN, -MARGIN, size + MARGIN, size + MARGIN )
    turtle.down()
    turtle.hideturtle()
    turtle.speed( speed )
    turtle.pensize( PEN_WIDTH )
    turtle.penup()
    turtle.setposition( 0, 0 )
    turtle.pendown()

def shrink(size: float):
    size = (((size/2)/math.sqrt(2)))
    return size

def drawsqr(size: float):
    turtle.color('blue')
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def rec_sqr(size: float, depth: int):
    if depth == 0:
        return
    else:
        turtle.color('orange')
        turtle.forward (size)
        turtle.left(90)
        turtle.forward (size/2)
        turtle.left(45)

        drawsqr(shrink(size))

        rec_sqr(shrink(size), depth -1)

        turtle.right(45)

        turtle.forward (size/2)
        turtle.left(90)
        turtle.forward (size)
        turtle.left(90)
        turtle.forward (size/2)
        turtle.left(45)

        drawsqr(shrink(size))

        rec_sqr(shrink(size), depth -1)

        turtle.right(45)
        
        turtle.forward (size/2)
        turtle.left(90)

        return

def main() -> None:
    """
    The main function prompts the user to enter a TT program.  It then expands
    that program to the basic TT commands and then executes them.
    :return: None
    """
    size = int(input('Enter the size of the sides:'))
    depth = int(input('Enter the depth:'))
    init(size, 100)
    rec_sqr(size, depth)

    print('Close the graphic window when done.')
    turtle.mainloop()


if __name__ == '__main__':
    main()