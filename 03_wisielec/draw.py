
import turtle
def draw(move_number):
    moves=[[40,0],[20,0,20,20],[20,70], [20, 140], [80, 140], [80, 100], [10], [80,80], [70,80], [90,80, 80,80], [80,60], [70,40,80,60], [90,40]]
    turtle.TurtleScreen._RUNNING = True
    d = turtle.Turtle()
    for move in range(0,move_number):
        if len(moves[move]) == 1:
            d.circle(moves[move][0])
        elif len(moves[move]) == 2:
            d.goto(moves[move][0],moves[move][1])
        elif len(moves[move]) == 4:
            d.goto(moves[move][0],moves[move][1])
            d.goto(moves[move][2], moves[move][3])
    turtle.exitonclick()

def main():
    draw(14)


if __name__ == '__main__':
    main()