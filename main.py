from turtle import *
import time
from snake import *
from food1 import Food
from scoreboard import ScoreBoard

thirai = Screen()
thirai.setup(width=1000, height=700)
thirai.bgcolor("black")
thirai.title("Snake game")
thirai.tracer(0)
snake = Snake()

game_over = False


thirai.listen()
thirai.onkey(snake.up, "Up")
thirai.onkey(snake.down, "Down")
thirai.onkey(snake.left, "Left")
thirai.onkey(snake.right, "Right")

food = Food()


# food.refresh_food()
scores = ScoreBoard()
while not game_over:
    thirai.update()
    time.sleep(0.06)
    snake.move_snake()


    if snake.segments[0].distance(food.p_food.xcor(), food.p_food.ycor()) < 20:
        food.refresh_food()
        snake.extend()
        scores.increase_score()

    if snake.segments[0].xcor() > 500 or snake.segments[0].xcor() < -500 or snake.segments[0].ycor() > 350 or \
            snake.segments[0].ycor() < -350:
        scores.high_score()
        scores.refresh()
        time.sleep(0.5)
        snake.refresh()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scores.high_score()
            time.sleep(0.5)
            snake.refresh()



thirai.exitonclick()
