from tkinter import *
from tkinter import simpledialog
from random import randint
import time, pickle, os
import getpass
def main():
    c = Canvas(bg = "black",height = "720",width = "1280")
    c.pack() 

    def load_data():
        global highscore,username, username_list, highscore_list
        if (os.path.exists("highscore.txt")):
            highscore = pickle.load(open("highscore.txt", "rb"))
            username = pickle.load(open("username.txt", "rb"))
            username_list = pickle.load(open("username_list.txt", "rb"))
            highscore_list = pickle.load(open("highscore_list.txt", "rb"))

    def save_data():
        global highscore, highscore, username_list, highscore_list
        pickle.dump(highscore, open("highscore.txt", "wb"))
        pickle.dump(username, open("username.txt", "wb"))
        print(username_list)
        for i in range(len(username_list)):
            if(username_list[i] == getpass.getuser() and len(username_list) > 0):
                username_list.pop(i)
                highscore_list.pop(i)
                i-=1

        username_list.append(username)
        highscore_list.append(highscore)
        pickle.dump(username_list, open("username_list.txt", "wb"))
        pickle.dump(highscore_list, open("highscore_list.txt", "wb"))


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
    global snake_x, snake_y, direction, score, key_, paused, highscore, game_ended, food_x, food_y, username, username_list, highscore_list
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
    username = getpass.getuser()
    username_list = []
    highscore_list = []
    load_data()
    print(username_list)
    print(highscore_list)
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
        c.config(bg = "green")
        c.create_text(640, 65, text= "LEADERBOARD " , fill = "#fff")
        c.create_text(50, 20, text= "Game over...\nyou Scored: " + str(score) , fill = "#fff")
        save_data()
        load_data()
        # DISPLAYING LEADERBOARD AND IN ASCENDING ORDER:
        username_highscore_list = []
        for z in range(len(username_list)):
            username_highscore_list.append([username_list[z], highscore_list[z]])
        def take_2nd_element(elem):
            for c in range(len(elem)):
                return elem[c][1]
        username_highscore_list.sort(key = take_2nd_element)
        print(username_highscore_list)
        m = 50
        for i in range (len(username_list)): 
            c.create_text(440, 100, text= "RANK" , fill = "#fff")
            c.create_text(640, 100, text= "USERNAME" , fill = "#fff")
            c.create_text(840, 100, text= "SCORE" , fill = "#fff")
            c.create_text(440, 100 + 50, text= i +1 , fill = "#fff")
            c.create_text(640, 100 + 50, text= username_list[i] , fill = "#fff")
            c.create_text(840, 100 + 50, text =str(highscore_list[i]), fill = "#fff")
            m+=50
        

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

# MAIN MENU:
bg_img = PhotoImage(file = "snake_bg.png")
start = Button(window, text = "Start Game ",height = 6, width = 18, bg = 'red', command = main)
quit = Button(window, text = "Quit Game",height = 6, width = 18, command = quit)
bg = Label(image = bg_img)
start.place(x = 450, y = 300)
quit.place(x = 650,y = 300)
bg.place(x = 220, y = 20)


window.mainloop()


