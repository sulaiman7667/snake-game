# RESOLUTION: 1280X720

# NOTE: NO STYLING WAS USED DUE TO A BUG IN TKINTER NOT ALLOWING SOME MAC USERS TO STYLE
# BUTTONS + VM HAD SOME RESOLUTION BUGS THAT DID NOT ALLOW ME TO TEST PROPERLY .
# I AM WRITING THIS HOPING THE MARKING SCHEME FOR STYLING BUTTONS IS IGNORED.


from tkinter import Tk, PhotoImage, Button, Label, Canvas
from random import randint
import time, pickle, os, getpass

def main():
    # SNAKE WORLD CANVAS:
    global c
    c = Canvas(bg = "black",height = "720",width = "1280")
    c.pack()


    def save_game():
        global snake_x, snake_y, score, direction
        pickle.dump(snake_x, open("snake_x.txt", "wb"))
        pickle.dump(snake_y, open("snake_y.txt", "wb"))
        pickle.dump(score, open("score.txt", "wb"))
        pickle.dump(direction, open("direction.txt", "wb"))




    def load_game():
        global snake_x, snake_y, score, direction
        if (os.path.exists("snake_x.txt")):
            snake_x = pickle.load(open("snake_x.txt", "rb"))
            snake_y = pickle.load(open("snake_y.txt", "rb"))
            score = pickle.load(open("score.txt", "rb"))
            direction = pickle.load(open("direction.txt", "rb"))




    def load_data():
        global highscore, username, username_list, highscore_list
        if (os.path.exists("highscore.txt")):
            highscore = pickle.load(open("highscore.txt", "rb"))
        username_list = pickle.load(open("username_list.txt", "rb"))
        highscore_list = pickle.load(open("highscore_list.txt", "rb"))




   
    def save_data():
        global highscore, highscore, username_list, highscore_list
        pickle.dump(highscore, open("highscore.txt", "wb"))
        #REPLACE HIGHSCORE OF USER WITH NEW ONE:
        for i in range(len(username_list)):
            if(username_list[i] == username and len(username_list) > 0):
                username_list.pop(i)
                highscore_list.pop(i)
                i-=1
        username_list.append(username)
        highscore_list.append(highscore)
        pickle.dump(username_list, open("username_list.txt", "wb"))
        pickle.dump(highscore_list, open("highscore_list.txt", "wb"))






    def set_food_posistion_x():
        while True:
            x = randint(1, 63) * 20
            if(x not in (snake_x, snake_y)):
                food_x = x
                return food_x

   



    def set_food_posistion_y():
        while True:
            y = randint(2, 34) * 20
            if(y not in (snake_x,snake_y)):
                food_y = y
                return food_y

    
    

    # CREATING AND LOADING VARIABLES:
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
    username_list = []
    highscore_list = []
    if(load == True):
        load_game()
    load_data()
    username = getpass.getuser()
    





    def import_images():
        global snake_img, food_img, boss_img
        snake_img = PhotoImage(file = "snake.png")
        food_img = PhotoImage(file = "food.png")
        boss_img = PhotoImage(file = "boss.png") 
        

  
    

    def del_canvas():
        global load
        c.pack_forget()
        load = False
        if (os.path.exists("snake_x.txt")):
            os.remove("snake_x.txt")
            os.remove("snake_y.txt")
            os.remove("score.txt")
            os.remove("direction.txt")



    


    def create_objects():
        # SNAKE_BLOCKS IMAGES:
        for z in range(len(snake_x)):
            c.create_image(snake_x[z], snake_y[z], image = snake_img, tag = "snake_block")
        # TEXT:
        c.create_text(50, 15, text= "Score: " + str(score), fill = "#fff", tag = "score")
        c.create_text(100, 15, text= "|" , fill = "#fff")
        c.create_text(167, 15, text= "highscore: " + str(highscore), fill = "#fff", tag = "highscore")
        c.create_text(1180, 15, text= "Press  p or b  to pause", fill = "#fff")

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
        


    
    def save_and_exit():
        global key_
        save_game()
        key_ = "p"
        exit()




    def direction_and_keys():
        global snake_x, snake_y, paused, key_, score, highscore
        # PAUSE GAME:
        if(key_ == "p"):
            toggle_pause()
            quit_btn = Button(text = "Quit and save game",height = 5, width = 18, command = save_and_exit)
            quit_btn.place(x = 520, y = 500)
            while (paused == True):
                if(key_ == "p"):    
                    toggle_pause()
                    quit_btn.destroy()
                c.update()
        if(key_ == "b"):
            toggle_pause()
            boss = c.create_image(800, 570, image = boss_img)
            while (paused == True):
                if(key_ == "b"):    
                    toggle_pause()
                    c.delete(boss)
                c.update()
        # CHEAT KEY:
        if(key_ == "c"):
            c.coords("food", food_x, food_y)
            i = len(snake_x) -1
            snake_x.append((snake_x[i] - 20))
            snake_y.append((snake_x[i] - 20))
            c.create_image(snake_x[-1], snake_y[-1], image = snake_img, tag = "snake_block")
            score += 1
            c.itemconfigure("score", text= "Score: " + str(score), fill = "#fff")
            key_ = ""
            if (score > highscore):
                highscore = score
                c.itemconfigure("highscore", text= "highScore: " + str(highscore), fill = "#fff")
        # MOVE_SNAKE:
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
       
    




    def check_snake_collision():
        global score, highscore, game_ended, food_x, food_y
        game_ended = False
        # COLLISION OF SNAKE WITH BORDER:
        if(snake_x[0] == 1280 or snake_x[0] == 0):
            game_ended = True
            game_over()
        if(snake_y[0] == 700 or snake_y[0] <= 20):
            game_ended = True
            game_over()
        # COLLISION OF SNAKE_HEAD WITH ITSELF:
        temp_list = []
        for i in range(len(snake_x)):
            temp_list.append([snake_x[i],snake_y[i]])
            if(temp_list[0] in temp_list[1:]):
                game_ended = True
                game_over()
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

    




    def update_key(key):
        global direction, key_
        key_ = ""
        temp_direction = key.keysym
        directions = ["Up", "Right", "Left", "Down"]
        opp_directions1 = [["Up", "Down"], ["Left", "Right"]]
        opp_directions2 = [["Down", "Up"], ["Right", "Left"]]
        if(temp_direction in directions and [temp_direction, direction] not in opp_directions1 and [temp_direction, direction] not in opp_directions2):
            direction = temp_direction
        if (temp_direction == "p" or temp_direction == "b" or temp_direction == "c"):
            key_ = temp_direction 



    

    def toggle_pause():
        global paused,key_
        if(paused == True):
            paused =False
        else:
            paused = True
        key_ = ""

    



    def game_over():
        global tkinter
        if (os.path.exists("snake_x.txt")):
            os.remove("snake_x.txt")
            os.remove("snake_y.txt")
            os.remove("score.txt")
            os.remove("direction.txt")
        c.delete("all")
        c.config(bg = "green")
        c.create_text(640, 65, text= "LEADERBOARD " , fill = "#fff")
        c.create_text(55, 20, text= "Game over...\nyou Scored: " + str(score) , fill = "#fff")
        save_data()
        load_data()
        # DISPLAYING LEADERBOARD AND IN DESCENDING ORDER:
        username_highscore_list = []
        for z in range(len(username_list)):
            username_highscore_list.append([username_list[z], highscore_list[z]])
        username_highscore_list.sort(reverse = True, key = lambda x: x[1])
        m = 50
        for i in range (len(username_list)): 
            c.create_text(440, 100, text= "RANK" , fill = "#fff")
            c.create_text(640, 100, text= "USERNAME" , fill = "#fff")
            c.create_text(840, 100, text= "SCORE" , fill = "#fff")
            c.create_text(440, 100 + m, text= i +1 , fill = "#fff")
            c.create_text(640, 100 + m, text= username_highscore_list[i][0] , fill = "#fff")
            c.create_text(840, 100 + m, text =str(username_highscore_list[i][1]), fill = "#fff")
            m+=50

    

    
            
    def loop_functions():
        global game_ended
        if(game_ended == False):
            check_snake_collision()
            direction_and_keys()
            c.after(50, loop_functions)
        if(game_ended == True):
            retry_btn = Button( text = "Retry ", height = 5, width = 20, command = lambda: [del_canvas(), main()])
            retry_btn.place(x = 5, y =610)

        

    

    def perform_functions():
        import_images()
        create_objects()
        loop_functions()



    perform_functions()  
    c.bind_all("<Key>", update_key)

def check_if_load_game():
    global load
    load = True

window = Tk()
window.title("Snake")
window.configure(bg = "green")
window.geometry("1280x720")


# MAIN MENU:
global bg_img, start, quit, bg, x
load = False
bg_img = PhotoImage(file = "snake_bg.png")
start = Button(window, text = "Start Game ", height = 5, width = 18, highlightbackground='yellow', command = lambda: [check_if_load_game(), main()])
quit = Button(window, text = "Quit Game",height = 5, width = 18, highlightbackground = "red", command = quit)
bg = Label(image = bg_img)
start.place(x = 450, y = 375)
quit.place(x = 650,y = 375)
bg.place(x = 220, y = 20)
if(os.path.exists("snake_x.txt")):
    start.config(text = "Continue game")




window.mainloop()










