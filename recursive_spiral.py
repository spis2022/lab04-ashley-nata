import turtle
t = turtle.Turtle()

def spiral(initial_length, angle, multiplier):
    print(initial_length)
    #base case
    if initial_length < 1:
        pass
    elif initial_length > 500:
        pass
    #recursive case
    else:
        t.forward(initial_length)
        t.right(angle)
        spiral(initial_length*multiplier, angle, multiplier)



