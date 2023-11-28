import tkinter as tk
import time
from PIL import Image, ImageTk
import ctypes

class ClientWindow(tk.Frame):

    def __init__(self, root):
        
        super().__init__(
            root,
            bg = "White"
        )
        
        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        self.label_gif1 = tk.Label(
            self.main_frame,
            bg='white',
            border=0,
            highlightthickness=0
        )
        
        self.label_gif1.grid(column=0, row=0)

        self.gif1_frames = self._get_frames('graphical assets/mrmoulder.gif')

        root.after(100, self._play_gif(self.label_gif1, self.gif1_frames))

        self.button = tk.Button(
            self.main_frame,
            text="Button",
            width=10,
            height=2
        )
        self.button.grid(column=0, row=1)


    def _get_frames(self, img):
        with Image.open(img) as gif:
            index = 0
            frames = []
            while True:
                try:
                    gif.seek(index)
                    frame = ImageTk.PhotoImage(gif)
                    frames.append(frame)
                except EOFError:
                    break
                
                index += 1

            return frames
        
    def _play_gif(self, label, frames):
        
        total_delay = 50
        delay_frames = 100

        for frame in frames:
            root.after(total_delay, self._next_frame, frame, label)
            total_delay+= delay_frames
    
    def _next_frame(self, frame, label):
        label.config(
            image = frame
        )

#initialize window
root = tk.Tk()
root.title("DistributedSystem Client Program")
root.geometry("300x300+50+50")

def init_window():
    user32 = ctypes.windll.user32
    screenwidth = user32.GetSystemMetrics(0)
    screenheight = user32.GetSystemMetrics(1)
    print(screenheight, screenwidth)

    WindowInstance = ClientWindow(root)

    root.mainloop()