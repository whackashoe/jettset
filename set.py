iterations = 2000; #amount of times function iterated before escape
magic      = 2000; #used as starting number for bottom result
#used for scaling virtual canvas, bigger is smaller
#it is easier to see for me when scaleY shrunken to 100th of scaleX
scaleX     = 10000.0;
scaleY     = 100.0;
#used for moving around virtual canvas
offsetX    = 3500000.0;
offsetY    = 30000.0;


# the first two top numbers and first bottom number is supplied,
# in my setup I set screenX, screenY, magic and the starting variables
# the previous top number is divided by the current top number and this is added to the result of the previous bottom number

# e.g. (rounded)

# 1(x)     1.62(y)     0.62    3.23
# 0(magic)    0.62      2.61   0.19

# we feed x, y, and magic number and returning iteration dictates color


def jset(a, b, c):
    for i in range(x, iterations):
        d = a/b;  #new bottom number
        e = c+d;  #new top number

        a = b;    #move b to the left
        b = e;    #add new b
        c = d;    #add new c
        if (a == 2.0 and b == 2.0 and c == 1.0):
            return i; #finite sequence

    return -1; #infinite sequence in scope


#an example drawing function

def draw_jset():
    for y in range(0, 10):
        for x in range(0, 10):
            j = jset(offsetX + (x*scaleX), offsetY + (y*scaleY), magic);
            if (j >= 0):
                drawPoint(x, y, j); #your function that can map j to a color