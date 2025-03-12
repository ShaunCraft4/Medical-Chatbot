from pygame.locals import *
from pygame import mixer
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font


mixer.init()
mixer.music.load("Loginand2ndpagesong.wav")


def nextpage():
    root1.destroy()
    import SPARK_X_page_3


def musiconoff():
    if btn_music["text"] == "Play":
        btn_music["text"] = "Pause"
        mixer.music.play(loops=-1)
    else:
        btn_music["text"] = "Play"
        mixer.music.pause()


root1 = tk.Tk()
root1.title("Successful Login")
root1.config(bg="#76EE00")
root1.geometry("800x800")
root1.resizable(width=False, height=False)


label= tk.Label(root1,font=("Arial",25,"bold"),text="Please click the button below to go to the chatbot:",foreground="black",bg="cyan")
label.pack()


original_image = Image.open(r"C:\Users\shaun\Downloads\SPARK-X-2023\dist\chatbot2.png")
converted_image = (original_image.resize((700, 400))).convert("RGB")
converted_image.save("converted_image.gif", "GIF")
image = tk.PhotoImage(file="converted_image.gif")
label_image = tk.Label(root1, image=image,padx=100,pady=100)
label_image.place(x=50,y=125)


btn_chatbot=Button(root1, font=("Arial",25,"bold"),text="Chatbot",bg="#FFB90F",command=nextpage, foreground="black",height="3",width="20")
btn_chatbot.place(x=100,y=600)


label_music= tk.Label(root1, font=("Arial",25,"bold"), text="Music:",foreground="black",bg="cyan")
label_music.place(x=600,y=600)



btn_music = tk.Button(root1, font=("Arial",25,"bold"), text="Play",foreground="black", command=musiconoff,bg="#FFB90F")
btn_music.place(x=608,y=675)


root1.mainloop()