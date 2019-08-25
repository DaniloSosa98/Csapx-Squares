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
SHRINKAGE = 1 / 3

def probsolv_1( _: int ):
    """
    Move the turtle to the proper position and heading to draw the first
    nested (depth-1) square, assuming that the turtle is in the position and
    heading it would be in after having drawn the square at the current depth.
    This function moves the turtle to the proper spot for the problem-solving
    session assignment.
    :param _: (unused) the length of a side of a square at the current depth
    """
    pass

def probsolv_2( side_size: int ):
    """
    Move the turtle to the proper position and heading to draw the second
    nested (depth-1) square, assuming that the turtle is in the position and
    heading it would be in after having drawn the square at the current depth.
    This function moves the turtle to the proper spot for the problem-solving
    session assignment.
    :param side_size: the length of a side of a square at the current depth
    """
    turtle.forward ( side_size * ( 1 - SHRINKAGE ) )
    turtle.left( 90 )
    turtle.forward ( side_size * ( 1 - SHRINKAGE ) )
    turtle.right( 90 )

move_to_subsquare_1 = probsolv_1
move_to_subsquare_2 = probsolv_2
