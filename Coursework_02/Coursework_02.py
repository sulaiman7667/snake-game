from tkinter import *
window = Tk()
window.title("Snake")
window.geometry("700x700")
window.configure(bg = "black")
c = Canvas(bg = "black",height = "700",width = "700")
c.pack()



snake_x = [400, 380, 360]
snake_y = [400, 400, 400]
food_x = [200]
food_y = [200]
score = 0
highscore = 0
direction = "Right"
def import_images():
    global snake_img, food_img
    snake_img = PhotoImage(file = "snake.png")
    food_img = PhotoImage(file = "food.png")


def create_objects():
    for z in range(len(snake_x)):
        c.create_image(snake_x[z], snake_y[z], image = snake_img, tag = "snake_block")
    c.create_text(50, 10, text= "Score: " + str(score), fill = "#fff", tag = "score")
    c.create_text(150, 10, text= "highscore: " + str(highscore), fill = "#fff")
    c.create_rectangle(10, 20, 700, 700, outline = "#525d69")
    c.create_image(food_x[0], food_y[0], image = food_img)

def move_snake():
    global snake_x, snake_y
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
    if(snake_x[0] == 700 or snake_x[0] == 0):
        quit()
    if(snake_y[0] == 700 or snake_y[0] == 0):
        quit()
    temp_list = []
    for i in range(len(snake_x)):
        temp_list.append([snake_x[i],snake_y[i]])
        if(temp_list[0] in temp_list[1:]):
            quit()
    if(snake_x[0] == food_x[0] and snake_y[0] == food_y[0]):
        i = len(snake_x) -1
        snake_x.append((snake_x[i] - 20))
        snake_y.append((snake_x[i] - 20))
        c.create_image(snake_x[-1], snake_y[-1], image = snake_img, tag = "snake_block")
        score += 1
        c.itemconfigure("score", text= "Score: " + str(score), fill = "#fff")
def update_direction(key):
    global direction
    temp_direction = key.keysym
    directions = ["Up", "Right", "Left", "Down"]
    opp_directions1 = [["Up", "Down"], ["Left", "Right"]]
    opp_directions2 = [["Down", "Up"], ["Right", "Left"]]
    if(temp_direction in directions and [temp_direction, direction] not in opp_directions1 and [temp_direction, direction] not in opp_directions2):
        direction = temp_direction
    

def loop_action():
    check_snake_collision()
    move_snake()
    c.after(65, loop_action)

def perform_all_functions():
    import_images()
    create_objects()
    loop_action()

perform_all_functions()  

 





  
    



c.bind_all("<Key>", update_direction)


  



window.mainloop()
