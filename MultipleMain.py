from customtkinter import *
from PIL import ImageTk, Image
import Fragen
import random
import Antworten

number = 0
counter = 0




root = CTk()
root.title("Multiple choice FFW Fragen")
root.minsize(600,700)
root.geometry("600x600+50+50")

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)


anzahl = CTkLabel(root, text="x/y")
headline = CTkLabel(root, text=f"Gefahrentafel 1")
picture = CTkLabel(root, fg_color="black", width=250, height=250, text="")
buttonLable = CTkFrame(root, width=500, height=300)

# Create buttons
buttonTL = CTkButton(buttonLable, text="Top Left", width=240, height=140, command = lambda: check_right(buttonTL), font = ("font",18) )
buttonTL._text_label.configure(wraplength=200)
buttonTR = CTkButton(buttonLable, text="Top Right", width=240, height=140, command = lambda: check_right(buttonTR), font = ("font",18))
buttonTR._text_label.configure(wraplength=200)
buttonBL = CTkButton(buttonLable, text="Bottom Left", width=240, height=140, command = lambda: check_right(buttonBL), font = ("font",18))
buttonBL._text_label.configure(wraplength=200)
buttonBR = CTkButton(buttonLable, text="Bottom Right", width=240, height=140, command = lambda: check_right(buttonBR), font = ("font",18))
buttonBR._text_label.configure(wraplength=200)
print(buttonBR.cget("font"))
# print(buttonBR.cget("hover_color"))
# Place buttons
buttonTL.place(relx=0, rely=0, anchor='nw')
buttonTR.place(relx=1.0, rely=0, anchor='ne')
buttonBL.place(relx=0, rely=1.0, anchor='sw')
buttonBR.place(relx=1.0, rely=1.0, anchor='se')

# Add buttons to the list
buttonList = [buttonTL,buttonTR,buttonBL,buttonBR]
# print(buttonList)

nxt_button = CTkButton(root, text= "Next Question", command = lambda: next_question())


anzahl.pack(pady = 0)
headline.pack(pady = 0)
picture.pack(pady = 10)
buttonLable.pack(pady = 10)
nxt_button.pack(pady = 10)




def init():
    # load questions
    global order
    global anzahl_insgesamt
    fragen = Fragen.fragen
    order = list(range(1,21))
    anzahl_insgesamt = len(order)
    # random order
    random.shuffle(order)
    print(order)
    # load answer
    global antworten
    antworten = Antworten.answers
    # print(antworten)



def update():
    global number
    global richtig
    global buttonList
    global counter
    global antworten
    counter += 1
    if len(order) == 0:
        exit()
    if order is not None:
        print(order)
        number = order[0]
        # update solution
        print(antworten[number][0])
        richtig = antworten[number][0]
        random.shuffle(antworten[number])

    # update anzahl
    anzahl.configure(text = f"{counter}/{anzahl_insgesamt}")
    # update headline
    headline.configure(text = f"Gefahrentafel {number}")
    # update icon
    pic = Image.open(f"./icons/{number}.png")
    original_width, original_height = pic.size
    new_height =  250
    new_width = int((new_height/ original_height) * original_width)
    resized_img = pic.resize((new_width,new_height))
    img = CTkImage(light_image = resized_img, size=(new_width, new_height))
    picture.configure(image = img)
    picture.image = img
    
    # update buttons
    i = 0
    for btn in buttonList:
        btn.configure(text = antworten[number][i],fg_color = "#3B8ED0", hover_color = "#36719F")
        i += 1

    

def check_right(selected):
    # print(selected.cget("text"))
    if selected.cget("text") == richtig:
        print("richtig")
        selected.configure(fg_color = "green", hover_color = "green")
    else: 
        print("falsch")
        selected.configure(fg_color = "red", hover_color = "red")
        
        for btn in buttonList:
            if btn.cget("text") == richtig:
                btn.configure(fg_color = "green", hover_color = "green")

def next_question():
    global order
    order.pop(0)
    update()

init()
update()
root.mainloop()