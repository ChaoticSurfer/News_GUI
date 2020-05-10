import re
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import scrolledtext
from tkinter import ttk

from scrap_news import scrapppping

info = scrapppping()[:35]

win = tk.Tk()
win.title = "news"
# for search

search_var = tk.StringVar()


def esc_destroy(event):
    yes = msg.askyesno('really?', 'Are you Sure you want to Quit??????')
    if yes:
        win.destroy()


def click_search():
    search_text = search.get()
    search_var.set(search_text)
    index = nb.index(nb.select())
    global info
    info = str(get_text_from_news(info[index]))
    answer = re.finditer(search_text, info)
    result = ''
    if answer:
        result += ' Match found! --> indexes(here):  '
        for i in answer:
            result += str(i.span())

    else:
        result = ':--> Not found'
    search_var.set(search_text + result)


def get_text_from_news(info):
    return f"{info['time']} --> {str(info['title'])}  \n\n {info['content']}"


# for iteration

screen_width = int(win.winfo_screenwidth())
screen_height = int(win.winfo_screenheight() * 85 // 100)
scPlus1 = 0  # int(win.winfo_screenwidth() * 7.5 // 100)
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

tk.Label(LF1, textvariable=search_var).pack()
tk.Label(win, text="search what what are you intereseted in").pack(side='left')
search = tk.Entry(win)
search.pack(side='right', fill='x', expand=1)
but1 = ttk.Button(win, text="Search", command=click_search).pack(side='left')
win.bind('<Escape>', esc_destroy)

win.mainloop()
