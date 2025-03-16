import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()

screen.setup(width=600, height=400)
screen.title("My snake Game")
screen.bgcolor("black")
screen.tracer(0)
time.sleep(1.5)
scoreboard = Scoreboard()
snake = Snake()
food = Food()

key_mapping = {"Up": "up", "Down": "down", "Left": "left", "Right": "right"}


def debug_move(action):
    print(f"Action: {action}")
    snake.move_direction(action)


screen.listen()

for key, action in key_mapping.items():
    print(f"Binding {key} to action {action}")
    screen.onkey(lambda action=action: debug_move(action), key)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    snake.move()

    if snake.collision_with_food(food):
        snake.grow()
        food.refresh()
        scoreboard.increase_score()

    if snake.collision():
        game_is_on = False
        print("Game Over! You lose!")

screen.mainloop()
screen.exitonclick()
