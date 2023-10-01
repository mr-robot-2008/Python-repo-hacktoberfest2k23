import turtle as t

def forward(distance):
    t.forward(distance)

def backward(distance):
    t.backward(distance)

def left(angle):
    t.left(angle)

def right(angle):
    t.right(angle)

def penup():
    t.penup()

def pendown():
    t.pendown()

def clear():
    t.clear()

def reset():
    t.reset()

def circle(radius):
    t.circle(radius)

def square(side_length):
    for _ in range(4):
        forward(side_length)
        right(90)

def triangle(side_length):
    for _ in range(3):
        forward(side_length)
        right(120)

def pentagon(side_length):
    for _ in range(5):
        forward(side_length)
        right(72)

def hexagon(side_length):
    for _ in range(6):
        forward(side_length)
        right(60)

def main():
    # Set up the turtle screen
    t.speed(1)
    t.title("Extended Turtle Graphics")

    # Define commands
    commands = {
        "FD": forward,
        "BK": backward,
        "RT": right,
        "LT": left,
        "PU": penup,
        "PD": pendown,
        "CLEAR": clear,
        "RESET": reset,
        "CIRCLE": circle,
        "SQUARE": square,
        "TRIANGLE": triangle,
        "PENTAGON": pentagon,
        "HEXAGON": hexagon
    }

    while True:
        user_input = input("Enter Logo command (e.g., 'FD 100', 'RT 90', 'CLEAR', 'RESET', 'CIRCLE 50', 'SQUARE 80', 'EXIT'): ").upper()
        if user_input == "EXIT":
            break

        parts = user_input.split()
        command = parts[0]
        if command in commands:
            try:
                argument = int(parts[1])
                commands[command](argument)
            except IndexError:
                commands[command]()
            except ValueError:
                print("Invalid argument. Please enter a number.")

    t.done()

if __name__ == "__main__":
    main()
