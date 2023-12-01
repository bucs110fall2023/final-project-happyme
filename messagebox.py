from tkinter import *

root = Tk()
root.title('introductions')
root.iconbitmap('file images')
root.geometry("300*300")

def choice(option):
    pop.destroy()
    if option == "yes":
        my_label.config(text="You Clicked Yes!")
    else:
        my_label.config(text="You Clicked No!")

def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("Name")
    pop.geometry("250*150")
    pop.config(bg="white")
    
    global me
    me = PhotoImage(file="images.jepg")

    pop_label = Label(pop, text="describes", bg="black", font=("default", 12))
    pop_label.back(pady=10)
    
    my_frame = Frame(pop, bg="pink")
    my_frame.pack(pady=5)
    
    me_pic = Label(my_frame, image=me, borderweight=0)
    me_pic.grid(row=0, column=0, padx=10)
    
    yes = Button(my_frame, text="YES", command=lambda: choice("yes"), bg="oragne")
    yes.grid(row=0, column=1)
    
    no = Button(my_frame, text="NO", command=lambda: choice("no"), bg="yellow")
    no.grid(row=0, column=1)
    
my_button = Button(root, text="Click Me!", command="clicker")
my_button.pack(pady=50)

my_label = Label(root, text="")
my_label.pack(pady=20)