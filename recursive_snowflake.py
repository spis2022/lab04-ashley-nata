import turtle
t = turtle.Turtle()
def snowflake_side(side_length, levels):
    if levels == 0:
        t.forward(side_length)
    else:
        distance = side_length * (1/3)
        snowflake_side(distance, levels-1)        
        t.right(60)
        snowflake_side(distance, levels-1)
        t.left(120)
        snowflake_side(distance, levels-1)
        t.right(60)
        snowflake_side(distance, levels-1)    

    
def snowflake(side_length, levels):
    snowflake_side(side_length, levels)
    t.left(120)
    snowflake_side(side_length, levels)
    t.left(120)
    snowflake_side(side_length, levels)
    
        