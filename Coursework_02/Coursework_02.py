from tkinter import *
from random import randint
window = Tk()
window.title("Snake")
window.geometry("1280x720")
window.configure(bg = "black")
c = Canvas(bg = "black",height = "720",width = "1280")
c.pack()

def set_food_posistion_x():
    while True:
        global food_x, x
        x = randint(1, 62) * 20
        if(x not in snake_x):
            food_x = x
            return food_x
def set_food_posistion_y():
    global food_y, y
    while True:
        y = randint(2, 34) * 20
        if(y not in snake_y):
            food_y = y
            return food_y

snake_x = [400, 380, 360]
snake_y = [400, 400, 400]
food_x = set_food_posistion_x()
food_y = set_food_posistion_y()
score = 0
highscore = 0
direction = "Right"
def import_images():
    global snake_img, food_img
    snake_img = PhotoImage(file = "snake.png")
    food_img = PhotoImage(file = "food.png") # 30 90 150 210
    # 50 110 140
    # 40 

def create_objects():
    for z in range(len(snake_x)):
        c.create_image(snake_x[z], snake_y[z], image = snake_img, tag = "snake_block")
    c.create_text(50, 10, text= "Score: " + str(score), fill = "#fff", tag = "score")
    c.create_text(150, 10, text= "highscore: " + str(highscore), fill = "#fff", tag = "highscore")
    c.create_rectangle(0, 25, 1280, 720, outline = "#000000")
    i = 0
    for m in range(21):
        # VERTICAL LINES
        c.create_line(30 + i, 30, 30 + i, 690, fill="#476042")
        c.create_line(50 + i, 30, 50 + i, 690, fill="#476042")
        c.create_line(10 + i, 30, 10 + i, 690, fill="#476042")
        #HORIZONTAL LINES
        c.create_line(10, 30+i, 1250, 30+i, fill="#476042")
        c.create_line(10, 70+i, 1250, 70+i, fill="#476042")
        c.create_line(10, 50+i, 1250, 50+i, fill="#476042")
        
        i+= 60
    c.create_image(food_x, food_y, image = food_img, tag = "food")

def move_snake():
    global snake_x, snake_y
    if(direction == "p"):
        time.sleep(10)
    if(direction == "Right"):
        new_x = snake_x[0] + 20
        new_y = snake_y[0]
    if(direction == "Left"):
        new_x = snake_x[0] - 20
        new_y = snake_y[0]
    if(direction == "Up"):
        new_x = snake_x[0]
        new_y = snake_y[0] - 20
    if(direction == "Down"):
        new_x = snake_x[0]
        new_y = snake_y[0] + 20
        
    snake_x = [new_x] + snake_x[:-1]
    snake_y = [new_y] + snake_y[:-1]
    

    for tag, x, y in zip(c.find_withtag("snake_block"), snake_x, snake_y):
        c.coords(tag, x, y)
   
    
def check_snake_collision():
    global score
    global food_x, food_y
    if(snake_x[0] == 1260 or snake_x[0] == 0):
        quit()
    if(snake_y[0] == 700 or snake_y[0] <= 20):
        quit()
    temp_list = []
    for i in range(len(snake_x)):
        temp_list.append([snake_x[i],snake_y[i]])
        if(temp_list[0] in temp_list[1:]):
            quit()
    if(snake_x[0] == food_x and snake_y[0] == food_y):
        food_x = set_food_posistion_x()
        food_y = set_food_posistion_y()
        c.coords("food", food_x, food_y)
        i = len(snake_x) -1
        snake_x.append((snake_x[i] - 20))
        snake_y.append((snake_x[i] - 20))
        c.create_image(snake_x[-1], snake_y[-1], image = snake_img, tag = "snake_block")
        score += 1
        c.itemconfigure("score", text= "Score: " + str(score), fill = "#fff")
        if (score > highscore):
            c.itemconfigure("highscore", text= "highScore: " + str(score), fill = "#fff")


def update_direction(key):
    global direction
    temp_direction = key.keysym
    directions = ["Up", "Right", "Left", "Down"]
    opp_directions1 = [["Up", "Down"], ["Left", "Right"]]
    opp_directions2 = [["Down", "Up"], ["Right", "Left"]]
    if(temp_direction in directions and [temp_direction, direction] not in opp_directions1 and [temp_direction, direction] not in opp_directions2):
        direction = temp_direction
    if (temp_direction == "p"):
        direction = temp_direction 
    

def loop_functions():
    check_snake_collision()
    move_snake()
    c.after(55, loop_functions)

def perform_all_functions():
    import_images()
    create_objects()
    loop_functions()

perform_all_functions()  
c.bind_all("<Key>", update_direction)
window.mainloop()
