from tkinter import *
import ctypes





#Get screen size
def init_window():
    user32 = ctypes.windll.user32
    screenwidth = user32.GetSystemMetrics(0)
    screenheight = user32.GetSystemMetrics(1)
    print(screenheight, screenwidth)
    #initialize window
    root = Tk()
    root.title("DistributedSystem Program")
    root.configure(background="cyan")
    root.minsize(200,200)
    root.geometry("300x300+50+50")

    

    #Create label
    text = Label(root, text="lol", background="green")
    text.pack()
    text2 = Label(root, text="lmao, even")
    text2.pack()
    image=PhotoImage(file="graphical assets/mrmoulder.gif")
    img = Label(root, image=image)
    img.pack()
    entry1 = tk.Entry(root)
    entry1.pack()


    root.mainloop()