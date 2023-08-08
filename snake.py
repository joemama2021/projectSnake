import turtle
import random
import time

player_score = 0
high_score = 0
delay_time = 0.10

#WINDOW CREATION#
window = turtle.Screen()
window.title("Snake Game Project")
window.bgcolor(0,0,0)
window.setup(width = 800, height = 600)
 

#CREATING BODY#
snake = turtle.Turtle()
snake.shape("circle")
snake.color("white")
snake.penup()
snake.goto(0,0)
snake.direction = "Stop"


#CREATING FOOD#
food = turtle.Turtle()
food.shape('square')
food.color("white")
food.speed(0)
food.penup()
food.goto(0, 100)


#PRINTING AND DISPLAY#
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,270)
pen.write("Your Score: 0\nHighest Score: 0", align = "center")
font = ("Arial", 25, "bold")



#########################################################################
#MOVEMENT AND DIRECTION#

def move_left():
    if snake.direction != "right":
        snake.direction = "left"
    
def move_right():
    if snake.direction != "left":
        snake.direction = "right"
    
def move_up():
    if snake.direction != 'down':
        snake.direction = 'up'

def move_down():
    if snake.direction != 'up':
        snake.direction = 'down'

def helper_move():
    if snake.direction == 'up':
        cood = snake.ycor()
        snake.sety(cood+20)
    
    if snake.direction == 'down':
        cood = snake.ycor()
        snake.sety(cood-20)
    
    if snake.direction == 'left':
        cood = snake.xcor()
        snake.setx(cood-20)
    
    if snake.direction == 'right':
        cood = snake.xcor()
        snake.setx(cood+20)
    
    if snake.direction == 'Stop':
        cood = snake.xcor()
        snake.setx(cood+20)

window.listen()
window.onkeypress(move_left, 'a')
window.onkeypress(move_right, 'd')
window.onkeypress(move_up, 'w')
window.onkeypress(move_down, 's')

#########################################################################
#MAIN LOOP AND LOGIc#

part_body = []

while True:
    window.update()
    if snake.xcor() > 350 or snake.xcor() < -350 or snake.ycor() > 250 or snake.ycor() < -250:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "Stop"
        snake.shape("circle")
        snake.color("white")
        
        while len(part_body) != 0:
            to_remove = part_body.pop()
            to_remove.goto(1000,1000)
        player_score = 0
        delay_time = 0.1
        pen.clear()
        pen.write("Player's score: {} High Score:{}".format(player_score, high_score), align = "center", font=("Arial", 25, "bold"))

    if snake.distance(food) < 12:
        coord_x = random.randint(-230, 230)
        coord_y = random.randint(-230, 230)
        food.goto(coord_x, coord_y)

            #ADDING PARTS OF BODY#
        add_part = turtle.Turtle()
        add_part.speed(0)
        add_part.shape("circle")
        add_part.color("grey")
        add_part.penup()
        part_body.append(add_part)
        delay_time = delay_time - 0.01
        player_score = player_score + 2

        if player_score > high_score:
            high_score = player_score
            pen.clear()
            pen.write("Player score: {} High score: {}".format(player_score, high_score), align="center", font=("Arial", 25, "bold"))
        
    
    #COLLISION DETECTION#
    for i in range(len(part_body)-1, 0, -1):
        coord_x = part_body[i-1].xcor()
        coord_y = part_body[i-1].ycor()
        part_body[i].goto(coord_x, coord_y)

    if len(part_body) > 0:
        coord_x = snake.xcor()
        coord_y = snake.ycor()
        part_body[0].goto(coord_x, coord_y)

    helper_move()

    for parts in part_body:
        if parts.distance(snake) < 20:
            time.sleep(3)
            snake.goto(0,0)
            snake.direction = "Stop"
            snake.color("white")
            snake.shape("circle")

            while len(part_body) != 0:
                to_remove = part_body.pop()
                to_remove.goto(1000,1000)
            player_score = 0
            delay_time = 0.1
            pen.clear()
            pen.write("Player score: {} High score: {}".format(player_score, high_score), align="center", font=("Arial", 25, "bold"))
    
    time.sleep(delay_time)

turtle.mainloop()