import tkinter as tk
from tkinter import scrolledtext
import re
from tkinter import ttk
from scrap_news import scrapppping

info = scrapppping()

win = tk.Tk()
win.title = "news"

i1 = f"{info[0]['time']} --> {str(info[0]['title'])}  \n\n {info[0]['content']}"

screen_width = int(win.winfo_screenwidth() * 85 // 100)
screen_height = int(win.winfo_screenheight() * 85 // 100)
scPlus1 = int(win.winfo_screenwidth() * 7.5 // 100)
scPlus2 = int(win.winfo_screenheight() * 3 // 100)
win.iconbitmap(tk.PhotoImage('img/news.ico'))
win.geometry(f"{screen_width}x{screen_height}+{scPlus1}+{scPlus2}")
win.resizable(0, 0)

fl1 = tk.LabelFrame(win, text="View news").pack()


def create_text_widget(some_text):
    text = scrolledtext.ScrolledText(fl1, borderwidth=5, width=450)
    text.insert(0.0, some_text)
    text.configure(state='disabled')
    text.pack(fill='both', expand=1, padx=10)


create_text_widget(i1)

tk.Label(win, text="search what what are you intereseted in").pack(side='left')
ent = tk.Entry(win).pack(side='right', fill='x', expand=1)
but1 = ttk.Button(win, text="Search").pack(side='left')

win.mainloop()
