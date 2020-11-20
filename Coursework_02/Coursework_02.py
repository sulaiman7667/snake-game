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
def import_images():
    global snake_img, food_img
    snake_img = PhotoImage(file = "snake.png")
    food_img = PhotoImage(file = "food.png")


def create_objects():
    for z in range(len(snake_x)):
        c.create_image(snake_x[z], snake_y[z], image = snake_img, tag = "snake_block")
    c.create_text(50, 10, text= "Score: " + str(score), fill = "#fff")
    c.create_text(150, 10, text= "highscore: " + str(highscore), fill = "#fff")
    c.create_rectangle(10, 20, 700, 700, outline = "#525d69")
    c.create_image(food_x[0], food_y[0], image = food_img)

def move_snake():
    global snake_x
    for i in range (len(snake_x)):
        snake_x[i] = snake_x[i] + 20
    for tag, x, y in zip(c.find_withtag("snake_block"), snake_x, snake_y):
        c.coords(tag, x, y)

def loop_action():
    move_snake()
    check_snake_collision()
    c.after(65, loop_action)   
    
def check_snake_collision():
    if(snake_x[0] == 680 or snake_x[0] == 10):
        quit()
    if(snake_y[0] == 680 or snake_y[0] == 20):
        quit()
    if((snake_x[0] in snake_x[1:]) and (snake_y[0] in snake_y[1:])):
        quit()

def perform_all_functions():
    import_images()
    create_objects()
    loop_action()

perform_all_functions()  

 





  
    






  





     
window.mainloop()
