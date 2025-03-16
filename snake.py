from turtle import Screen
from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
screen = Screen()


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        start_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in start_positions:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segments.append(new_turtle)

    def move_direction(self, direction):
        current_heading = self.segments[0].heading()
        print("Move direction is working!")
        if direction == "up" and current_heading != 270:
            self.segments[0].setheading(90)
            print("up!")
        elif direction == "down" and current_heading != 90:
            self.segments[0].setheading(270)
            print("Down")
        elif direction == "left" and current_heading != 0:
            self.segments[0].setheading(180)
            print(("left"))
        elif direction == "right" and current_heading != 180:
            self.segments[0].setheading(0)
            print("right")

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
            self.segments[i].setheading(self.segments[i - 1].heading())

        self.segments[0].forward(20)

    def grow(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        last_segment = self.segments[-1]
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(new_segment)

    def collision_with_food(self, food):
        if self.head.distance(food) < 15:
            return True
        return False

    def collision(self):
        head = self.segments[0]
        if (
            head.xcor() > 290
            or head.xcor() < -290
            or head.ycor() > 190
            or head.ycor() < -190
        ):
            print("You have hit the wall!")
            return True

        for segment in self.segments[1:]:
            if head.distance(segment) < 10:
                print("You have hit your tale!")
                return True

        return False
