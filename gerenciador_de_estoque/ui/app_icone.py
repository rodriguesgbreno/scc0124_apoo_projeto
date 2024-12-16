import tkinter as tk
from tkinter import PhotoImage
import os

def set_icon(window):
    icon_path = "../assets/box.png"
    if os.path.isfile(icon_path):
        icon_image = PhotoImage(file=icon_path)
        window.iconphoto(False, icon_image)
    else:
        print(f"Arquivo de ícone não encontrado: {icon_path}")