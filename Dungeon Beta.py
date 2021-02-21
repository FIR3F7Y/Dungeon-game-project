import turtle
import math

# excludes treasure

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Dungeon Alpha")
wn.setup(700, 700)


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.gold = 0

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 24)
    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 24)
    def go_left(self):
        self.goto(self.xcor() - 24, self.ycor())
    def go_right(self):
        self.goto(self.xcor() + 24, self.ycor())
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() +24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    def is_collision(self, other):
        a = self.xcor() - other.xcor
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

levels = [""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX            XXX",
    "X  XXXXXXX           TXXX",
    "X       XX  XXXXX  XXXXXX",
    "XXX     XX  XXXXX  XXXXXX",
    "XXXXXX  XX  XXX      XXXX",
    "XXXXXX  XX  XXX      XXXX",
    "XXXXXX  XX  XXXXX  XXXXXX",
    "X  XXX       XXX   XXXXXX",
    "X  XX         XX   XXXXXX",
    "X      XXXXXXXX   XXXXXXX",
    "X               XXXXXXXXX",
    "XXXXXXXXX      XXXXXXXXXX",
    "XXX          XXXXXXXXXXXX",
    "XXX        XXXXXXXXXXXXXX",
    "XXX   XXXXXXXXXXXXXXXXXXX",
    "X     XXXXXXX      XXXXXX",
    "X     XXXXXXXXX    XXXXXX",
    "X                XXXXXXXX",
    "XX       XXXXXXXXXXXXXXXX",
    "XXXX        XXXXXXXXXXXXX",
    "XXXXXX        XXXXXXXXXXX",
    "XXXXXXXXXXX       XXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"]

treasures = []
levels.append(level_1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "P":
                player.goto(screen_x, screen_y)


pen = Pen()
player = Player()
walls = []
setup_maze(levels[1])
print(walls)
turtle.listen()
turtle.onkey(player.go_up, "w")
turtle.onkey(player.go_down, "s")
turtle.onkey(player.go_left, "a")
turtle.onkey(player.go_right, "d")
wn.mainloop()