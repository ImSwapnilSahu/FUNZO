from tkinter import *
import os

window = Tk()
window.title("Funzo")
window.config(padx=40, pady=40)

title_label = Label(text="Funzo", font=("Courier", 50, "bold"))
title_label.grid(column=1, row=0)

# ---------------------------- SNAKE ------------------------------- #
def open_snake_file():
    os.startfile("Snake_game.py")

snake = Canvas(width=210, height=224)
snake_img = PhotoImage(file="image/snake.png")
snake.create_image(108, 112, image=snake_img)
snake.grid(column=0, row=1)

snake_button = Button(text="Snake Game",width=20,height=2, command=open_snake_file)
snake_button.grid(column=0, row=2)

# ---------------------------- PONG ------------------------------- #
def open_pong_file():
    os.startfile("pong.py")

#pong = Canvas(padx=30, pady=30)
pong = Canvas(width=210, height=224)
pong_img = PhotoImage(file="image/pong.png")
pong.create_image(108, 112, image=pong_img)
pong.grid(column=1, row=1)

pong_button = Button(text="Pong Game",width=20,height=2, command=open_pong_file)
pong_button.grid(column=1, row=2)

# ---------------------------- TURTLE CROSSING ------------------------------- #
def open_turtle_file():
    os.startfile("turtle_crossing.py")

turtle = Canvas(width=210, height=224)
turtle_img = PhotoImage(file="image/turtle-crossing.png")
turtle.create_image(108, 112, image=turtle_img)
turtle.grid(column=2, row=1)

turtle_button = Button(text="Turtle Crossing Game",width=20,height=2, command=open_turtle_file)
turtle_button.grid(column=2, row=2)

window.mainloop()