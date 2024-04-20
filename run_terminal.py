from GDBOT import constants
import tkinter
import subprocess
import customtkinter
from PIL import Image, ImageTk

def change_token_on_click(token: str):

    if len(token) < 50:
        raise ValueError("Token must be at least 50 characters long")

    constants.TOKEN = token

def run_bot():
    subprocess.run(['run.bat'], shell=True)

def main():
    tk = tkinter.Tk()
    tk.title("GDBOT")
    tk.geometry('500x500')
    tk.resizable(False, False)
    tk.configure(bg='#AEF98D')
    image = Image.open(
        ""
        "images/title.png")
    image = image.resize((200, 200), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(image)


    image_label = tk.Label(tk, image=tk_image)
    image_label.pack()
    tk.mainloop()

if __name__ == '__main__':
    main()