from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import Fragen
import random

root = Tk()
root.title("Tk Example")
root.minsize(600, 600)  # width, height
root.geometry("600x600+50+50")


guess_var = StringVar()
number = 0
score = 0
answer = ""
counter = 1



fragen = Fragen.fragen
order = list(range(1,21))
random.shuffle(order)
print(order)

anzahlFragen = len(order)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    print (filename)
    return filename

def open_img(number):
    img = Image.open(f"./icons/{number}.png")
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

def submit():
    output.delete(1.0,END)
    guess = guess_var.get()
    print("guess was: "+ guess)
    print("answer is: "+ answer)
    if guess == answer:
        output.insert(END,f"Right: \n{answer}")
    else: 
        output.insert(END,f"Wrong: \n{answer}")

def func(event):
    # print("You hit return.")
    submit()
root.bind("<Return>",func)

def nextQuestion():
    global number
    global order
    global counter
    counter += 1
    print("Next Question clicked")
    print(order)
    if len(order) == 1:
        print(f"score: {score}")
        exit()
    else:
        order.pop(0)
    update()

def update():
    global number
    global order
    global answer
    global counter
    # print(fragen) 
    if order is not None:
        print(order[0])
        number = order[0] 
        answer = fragen.get(number)
        print(answer)
    headline.config(text = f"Gefahrentafel {counter}/{anzahlFragen}")

    img = Image.open(f"./icons/{number}.png")
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)
    panel.config(image = img)
    panel.image = img

    name_entry.delete(0,END)
    output.delete(1.0,END)
    





headline = Label(root, text=f"Gefahrentafel x")

img = Image.open(f"./icons/{number}.png")
img = img.resize((250, 250))
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img)
panel.image = img


ans_text = Label(root, text = "Antwort:")
output = Text(root, height = 5, width = 50, bg = "light cyan")

name_entry = Entry(root,textvariable = guess_var, width = 50, font=('calibre',11,'normal'))
sub_btn=Button(root,text = 'Submit', command = submit)
nxt_btn=Button(root,text = "Next Question", command = lambda: nextQuestion())


update()

headline.pack()
panel.pack()
ans_text.pack(pady = 5)
name_entry.pack(pady = 5)
sub_btn.pack(pady = 5)
output.pack(pady = 5)
nxt_btn.pack(pady = 5)


root.mainloop()