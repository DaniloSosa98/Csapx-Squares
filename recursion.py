import turtle
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

def finish():
    """
    Prepare to end the turtle graphics session.
    Wait for the user to close the window.
    """
    print( "Please close the turtle canvas window." )
    turtle.done()

# Length of highest depth square's side
BOX_SIZE = 1000

# By how much to reduce the square's sides at each successive depth
def try1(size: int ):
    shrink = int(size * (0.35))
    turtle.forward (size)
    turtle.left(90)
    turtle.forward (size/2)
    turtle.left(45)
    turtle.forward(shrink)
    turtle.left(90)
    turtle.forward(shrink)
    turtle.left(90)
    turtle.forward(shrink)
    turtle.left(90)
    turtle.forward(shrink)
    turtle.left(45)
    turtle.forward(size/2)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size/2)
    turtle.left(45)
    turtle.forward(shrink)
    turtle.left(90)
    turtle.forward(shrink)
    turtle.left(90)
    turtle.forward(shrink)
    turtle.left(90)
    turtle.forward(shrink)
    turtle.left(45)
    turtle.forward(size/2)
    turtle.left(90)

def main() -> None:
    """
    The main function prompts the user to enter a TT program.  It then expands
    that program to the basic TT commands and then executes them.
    :return: None
    """
    init(100, 1)
    try1(100)

    print('Close the graphic window when done.')
    turtle.mainloop()


if __name__ == '__main__':
    main()