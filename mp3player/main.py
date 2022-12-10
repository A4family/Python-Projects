import tkinter as tk
import fnmatch
import os
from pygame import mixer


canvas  = tk.Tk()
canvas.title("Music player")
canvas.geometry("600x800")
canvas.config(bg = 'black')
rootpath = "/home/a4family/Downloads/"
pattern = "*.mp3"

mixer.init()

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "//" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

listBox = tk.Listbox(canvas, fg = "cyan", bg = "black", width=100, font = ('poppins',14))
listBox.pack(padx=15,pady=15)

label = tk.Label(canvas,text="",bg="black",fg="yellow",font=('poppins',18))
label.pack(pady=15)

top = tk.Frame(canvas,bg = "black")
top.pack(padx = 10, pady=5, anchor="center")

prevButton = tk.Button(canvas, text="Prev")
prevButton.pack(pady= 15, in_=top, side="left")

stopButton = tk.Button(canvas, text="Stop", borderwidth=0, command=stop)
stopButton.pack(pady= 15, in_=top, side="left")

playButton = tk.Button(canvas, text="Play", borderwidth=0, command=select)
playButton.pack(pady=15,in_=top, side="left")

pauseButton = tk.Button(canvas,text="pause")
pauseButton.pack(pady=15,in_=top, side="left")

nextButton = tk.Button(canvas,text="Next")
nextButton.pack(pady=15, in_=top, side="left")


for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end',filename)


canvas.mainloop()

