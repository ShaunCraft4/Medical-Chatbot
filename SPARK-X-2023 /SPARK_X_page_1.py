from pygame.locals import *
from pygame import mixer
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import tkinter.font as font


mixer.init()
mixer.music.load("Loginand2ndpagesong.wav")

   
def nextPage():
    root.destroy()
    import SPARK_X_page_2
    
    
def validate_login():
    username = entry_username.get()
    phone_number = entry_phone.get()
    gender = entry_gender.get()
    if not username or not phone_number or not gender:
        messagebox.showerror("Error", "Please fill in all the fields appropriately")
    else:
        a=0
        b=0
        for i in phone_number:
            if i in "abcdefghijklmnopqrstuvwxyz":
                a+=1
        for j in username:
            if j in "1234567890":
                b+=1
        if a>0 or b>0:
            messagebox.showerror("Error", "Please fill in all the fields appropriately")
        else:
            messagebox.showinfo("Success", "Login Successful!")
            nextPage()


def musiconoff():
    if btn_music["text"] == "Play":
        btn_music["text"] = "Pause"
        mixer.music.play()
    else:
        btn_music["text"] = "Play"
        mixer.music.pause()


root = tk.Tk()
root.title("Medical Chatbot Login Page")
icon = tk.PhotoImage(file="MCI.png")
root.iconphoto(True, icon)
font=font.Font(size=20)
label_top = tk.Label(root, text="Please enter the needed details appropriately",foreground="black",bg="cyan")
label_top["font"]=font
label_top.pack()
root.config(bg="#76EE00")
root.geometry("800x800")
root.resizable(width=False, height=False)
left_root= tk.Frame(root)
left_root.pack(side="left",padx=100,pady=100)
right_root= tk.Frame(root)
right_root.pack(side="right",padx=20,pady=20)


label_username = tk.Label(left_root, text="Name:",foreground="black",bg="cyan")
label_username["font"]=font
label_username.pack()
entry_username = tk.Entry(left_root)
entry_username["font"]=font
entry_username.pack()


label_phone = tk.Label(left_root, text="Phone Number:",foreground="black", bg="cyan")
label_phone["font"]=font
label_phone.pack()
entry_phone = tk.Entry(left_root)
entry_phone["font"]=font
entry_phone.pack()


label_gender = tk.Label(left_root, text="Gender:",foreground="black", bg="cyan")
label_gender["font"]=font
label_gender.pack()
entry_gender = tk.Entry(left_root,)
entry_gender["font"]=font
entry_gender.pack()


original_image = Image.open(r"C:\Users\shaun\Downloads\SPARK-X-2023\dist\image.jpg")
converted_image = (original_image.resize((400, 500))).convert("RGB")
converted_image.save("converted_image.gif", "GIF")
image = tk.PhotoImage(file="converted_image.gif")
label_image = tk.Label(right_root, image=image)
label_image.pack()


btn_login = tk.Button(left_root, text="Login",foreground="black", command=validate_login,bg="#FFB90F")
btn_login["font"]=font
btn_login.pack()


label_music= tk.Label(root, font=("Arial",20,"bold"), text="Music:",foreground="black",bg="cyan")
label_music.place(x=600,y=675)


btn_music = tk.Button(root, font=("Arial",20,"bold"), text="Play",foreground="black", command=musiconoff,bg="#FFB90F")
btn_music.place(x=608,y=725)


root.mainloop()
