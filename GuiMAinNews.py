import tkinter as tk
from tkinter import scrolledtext
import re
from tkinter import ttk
from scrap_news import scrapppping

info = scrapppping()[:35]

win = tk.Tk()
win.title = "news"


def get_text_from_news(info):
    return f"{info['time']} --> {str(info['title'])}  \n\n {info['content']}"


# for iteration

screen_width = int(win.winfo_screenwidth())
screen_height = int(win.winfo_screenheight() * 85 // 100)
scPlus1 = 0                 # int(win.winfo_screenwidth() * 7.5 // 100)
scPlus2 = int(win.winfo_screenheight() * 2 // 100)
win.iconbitmap(tk.PhotoImage('img/news.ico'))
win.geometry(f"{screen_width}x{screen_height}+{scPlus1}+{scPlus2}")
win.resizable(0, 0)

LF1 = tk.LabelFrame(win, text="View news").pack()

nb = ttk.Notebook(LF1)
nb.pack(side='top', expand=1, fill='both', padx=10, pady=10)


def create_text_widget(parent, some_text):
    text = scrolledtext.ScrolledText(parent, borderwidth=5, width=450)
    text.insert(0.0, get_text_from_news(some_text))
    text.configure(state='disabled')
    text.pack(fill='both', expand=1, padx=10)
    return text


def get_short_title(news):
    return " ".join(news['title'].split()[:2])


for news, num in zip(info, range(35)):
    exec(f'tab{num} = create_text_widget(nb, news)')
    exec(f'nb.add(tab{num}, text=get_short_title(news))')

tk.Label(win, text="search what what are you intereseted in").pack(side='left')
ent = tk.Entry(win).pack(side='right', fill='x', expand=1)
but1 = ttk.Button(win, text="Search").pack(side='left')

win.mainloop()
