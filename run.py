import tkinter as tk
from tkinter import messagebox
import customtkinter
import subprocess

def run() -> None:
    subprocess.run('run.bat')



def main():
    customtkinter.set_appearance_mode('System')
    customtkinter.set_default_color_theme('blue')

    app = customtkinter.CTk()
    app.geometry('356x224')
    app.title('GDBOT Admin')

    title = customtkinter.CTkLabel(app, text='GDBOT Admin')
    title.pack(padx=10, pady=10)

    download = customtkinter.CTkButton(app, text='Run', command=run)
    download.pack(padx=10, pady=10)
    app.mainloop()



if __name__ == ' __main__':
    main()