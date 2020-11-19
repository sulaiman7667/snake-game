from tkinter import *
window = Tk()
window.title("Snake")
window.geometry("1200x1200")
window.configure(bg = "black")
c = Canvas(bg = "black",height = "1200",width = "1200")
c.pack()



snake_x = [400, 380, 360]
snake_y = [400, 400, 400]



def import_images():
    global snake_img, food_img
    snake_img = PhotoImage(file = "snake.png")
    food_img = PhotoImage(file = "food.png")


def create_objects():
    for z in range(len(snake_x)):
        c.create_image(snake_x[z], snake_y[z], image = snake_img, tag = "snake_block")

    

def move_snake():
    global snake_x
    for i in range (len(snake_x)):
        snake_x[i] = snake_x[i] + 20
    for tag, x, y in zip(c.find_withtag("snake_block"), snake_x, snake_y):
        c.coords(tag, x, y)

def loop_action():
    move_snake()
    c.after(65, loop_action)   
    


def perform_all_actions():
    import_images()
    create_objects()
    loop_action()

perform_all_actions()  
 





  
    






  





     
window.mainloop()
