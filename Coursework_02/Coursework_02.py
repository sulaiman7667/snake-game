from tkinter import *
from tkinter import simpledialog
from random import randint
import time, pickle, os
def main():
    c = Canvas(bg = "black",height = "720",width = "1280")
    c.pack()

    def get_user_name():
        if(score == score):
            x = simpledialog.askstring(" ", "You set a new highscore! \nEnter your name to be displayed on the leaderboard:")
        
    def load_data():
        global highscore
        if (os.path.exists("highscore.txt")):
            highscore = pickle.load(open("highscore.txt", "rb"))

    def save_data():
        global highscore
        pickle.dump(highscore, open("highscore.txt", "wb"))

    ############################################################################################################################################

    def set_food_posistion_x():
        while True:
            x = randint(1, 63) * 20
            if(x not in snake_x):
                food_x = x
                return food_x

    ############################################################################################################################################

    def set_food_posistion_y():
        while True:
            y = randint(2, 34) * 20
            if(y not in snake_y):
                food_y = y
                return food_y

    ############################################################################################################################################
    global snake_x, snake_y, direction, score, key_, paused, highscore, game_ended, food_x, food_y
    snake_x = [400, 380, 360]
    snake_y = [400, 400, 400]
    food_x = set_food_posistion_x()
    food_y = set_food_posistion_y()
    score = 0
    highscore = 0
    direction = "Right"
    key_= ""
    paused = False
    game_ended = False
    load_data()
    print(highscore)
    ############################################################################################################################################

    def import_images():
        global snake_img, food_img
        snake_img = PhotoImage(file = "snake.png")
        food_img = PhotoImage(file = "food.png") 
        

    ############################################################################################################################################

    def create_objects():
        # SNAKE_BLOCKS IMAGES:
        for z in range(len(snake_x)):
            c.create_image(snake_x[z], snake_y[z], image = snake_img, tag = "snake_block")
        #  TEXT:
        c.create_text(50, 15, text= "Score: " + str(score), fill = "#fff", tag = "score")
        c.create_text(100, 15, text= "| " , fill = "#fff")
        c.create_text(150, 15, text= "highscore: " + str(highscore), fill = "#fff", tag = "highscore")
        c.create_text(1150, 15, text= "Press p to pause/unpause game", fill = "#fff")

        i = 0
        for m in range(22):
            # VERTICAL LINES:
            c.create_line(30 + i, 30, 30 + i, 690, fill="#476042")
            c.create_line(50 + i, 30, 50 + i, 690, fill="#476042")
            c.create_line(10 + i, 30, 10 + i, 690, fill="#476042")
            #HORIZONTAL LINES:
            c.create_line(10, 30+i, 1270, 30+i, fill="#476042")
            c.create_line(10, 70+i, 1270, 70+i, fill="#476042")
            c.create_line(10, 50+i, 1270, 50+i, fill="#476042")   
            i+= 60
        # FOOD IMAGES:
        c.create_image(food_x, food_y, image = food_img, tag = "food")

    ############################################################################################################################################

    def move_snake():
        global snake_x, snake_y, paused, key_
        if(key_ == "p"):
            toggle_pause()
            while (paused == True):
                if(key_ == "p"):    
                    toggle_pause()
                c.update()
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
        
        # CHANGE COORDINATES OF ALL SNAKE_BLOCKS:
        for tag, x, y in zip(c.find_withtag("snake_block"), snake_x, snake_y):
            c.coords(tag, x, y)
       
    ############################################################################################################################################    

    def check_snake_collision():
        global score, highscore, game_ended
        global food_x, food_y
        game_ended = False
        if(snake_x[0] == 1280 or snake_x[0] == 0):
            game_ended = True
            end_game()
        if(snake_y[0] == 700 or snake_y[0] <= 20):
            game_ended = True
            end_game()
        # COLLISION OF SNAKE WITH ITSELF:
        temp_list = []
        for i in range(len(snake_x)):
            temp_list.append([snake_x[i],snake_y[i]])
            if(temp_list[0] in temp_list[1:]):
                game_ended = True
                end_game()
        # COLLISION OF SNAKE_HEAD WITH FOOD:
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
                highscore = score
                c.itemconfigure("highscore", text= "highScore: " + str(highscore), fill = "#fff")

    ############################################################################################################################################

    def update_key(key):
        global direction
        global key_
        key_ = ""
        temp_direction = key.keysym
        print(temp_direction)
        directions = ["Up", "Right", "Left", "Down"]
        opp_directions1 = [["Up", "Down"], ["Left", "Right"]]
        opp_directions2 = [["Down", "Up"], ["Right", "Left"]]
        if(temp_direction in directions and [temp_direction, direction] not in opp_directions1 and [temp_direction, direction] not in opp_directions2):
            direction = temp_direction
        if (temp_direction == "p"):
            key_ = temp_direction 



    ############################################################################################################################################
    def toggle_pause():
        global paused,key_
        if(paused == True):
            paused =False
        else:
            paused = True
        key_ = ""






    ############################################################################################################################################

    def end_game():
        global tkinter
        c.delete("all")
        c.create_text(400, 400, text= "Game over...\nyou Scored: " + str(score) , fill = "#fff", tag = "score")
        get_user_name()
        save_data()

    ############################################################################################################################################

    def loop_functions():
        global game_ended
        if(game_ended == False):
            check_snake_collision()
        move_snake()
        c.after(55, loop_functions)

    ############################################################################################################################################

    def perform_all_functions():
        import_images()
        create_objects()
        loop_functions()

    ############################################################################################################################################

    perform_all_functions()  
    c.bind_all("<Key>", update_key)
window = Tk()
window.title("Snake")
window.geometry("1280x720")
window.configure(bg = "green")
bg_img = PhotoImage(file = "snake_bg.png")
start = Button(window, text = "Start Game ",height = 4, width = 12, bg = 'red', command = main)
quit = Button(window, text = "Quit Game",height = 4, width = 12, command = quit)
leaderboard = Button(window, text = "Leaderboard",height = 4, width = 12, command = quit)
bg = Label(image = bg_img)
start.place(x = 565, y = 250)
quit.place(x = 565,y = 450)
leaderboard.place(x = 565, y =350)
bg.place(x = 220, y = 20)


window.mainloop()


