import tkinter as tk
from tkinter import messagebox
import random
import pygame
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
import time

# Constants
KEY = '-------------------'
WINDOW_NAME = 'Mortal Kombat: Key Generator'
WINDOW_SIZE = '1024x768'
PHOTO_PATH = 'i.png'  # Path to your background image
FONT_PARAMETERS = ('Comic Sans MS', 24)  # A playful font
MUSIC_FILE = 'mk.mp3'  # Mortal Kombat theme music file
GEN_BTN = 'Generate Key'
CANCEL_BTN = 'x'
FIELD_NAME = 'Your Mortal Kombat Key'
BTN_BG_COLOR = '#FF0000'  # Red color for the button
BTN_TEXT_COLOR = '#FFFF00'  # Yellow text color for the button
ALPHABET = 'QWERTYUIOPASDFGHJKLZXCVBNM0123456789'

def close():
    window.destroy()
    pygame.mixer.music.stop()

def key_gen():
    global KEY
    create_progressbar()
    KEY = ''
    
    # Generate 4 groups of keys
    for i in range(4):
        sub_key = ''.join(random.choices(ALPHABET, k=4))  # Generate a 4-character string
        KEY += sub_key
        if i < 3:  # Add hyphen after the first three groups
            KEY += '-'

    key_lbl.configure(text=f'{FIELD_NAME}: {KEY}')
    return KEY

def create_progressbar():
    prog_bar = Progressbar(window, orient='horizontal', length=440, mode='determinate')
    prog_bar.place(x=290, y=700)  # Adjust this if necessary for your layout
    for row in range(100):
        prog_bar['value'] = row
        window.update_idletasks()
        time.sleep(0.01)
    prog_bar.destroy()

if __name__ == '__main__':  # Corrected the name check
    window = tk.Tk()
    window.title(WINDOW_NAME)
    window.geometry(WINDOW_SIZE)

    # Load background image using Pillow
    bg_img = Image.open(PHOTO_PATH)
    bg_img_tk = ImageTk.PhotoImage(bg_img)

    lbl_bg = tk.Label(window, image=bg_img_tk)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

    # Generate Key Button
    btn_gen = tk.Button(window, text=GEN_BTN, width=20, command=key_gen, bg=BTN_BG_COLOR, fg=BTN_TEXT_COLOR, font=FONT_PARAMETERS, bd=15)
    btn_gen.place(relx=0.5, rely=0.85, anchor='center')

    # Close Button
    btn_cl = tk.Button(window, text=CANCEL_BTN, width=2, height=1, command=close, bg=BTN_BG_COLOR, fg=BTN_TEXT_COLOR, font=FONT_PARAMETERS, bd=15)
    btn_cl.place(relx=0.75, rely=0.85, anchor='center')

    # Key Label
    key_lbl = tk.Label(window, text=f'{FIELD_NAME}: {KEY}', font=('Comic Sans MS', 30), bg='black', fg='white', borderwidth=10, relief=tk.RAISED)
    key_lbl.place(relx=0.5, rely=0.73, anchor='center')

    # Initialize Pygame for music playback
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_FILE)
    pygame.mixer.music.play(-1)  # Loop the music

    # Start the main loop
    window.mainloop()




