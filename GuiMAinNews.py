import tkinter as tk
from tkinter import scrolledtext
import tkinter
from scrap_news import scrapppping

info = scrapppping()

win = tk.Tk()
win.title = "news"

var_st1 = tk.StringVar()

i1 = f"{info[0]['time']} --> {str(info[0]['title'])}  \n\n {info[0]['content']}"

var_st1.set(i1)

screen_width = int(win.winfo_screenwidth() * 85 // 100)
screen_height = int(win.winfo_screenheight() * 85 // 100)
scPlus1 = int(win.winfo_screenwidth() * 7.5 // 100)
scPlus2 = int(win.winfo_screenheight() * 3 // 100)
win.iconbitmap(tk.PhotoImage('img/news.ico'))
win.geometry(f"{screen_width}x{screen_height}+{scPlus1}+{scPlus2}")
win.resizable(0, 0)

fl1 = tk.LabelFrame(win, text="View news")
fl1.pack()

scrolledtext.ScrolledText(fl1, borderwidth=3, textvariable=var_st1, width=500, state='disabled').pack(fill='both',expand='yes')



win.mainloop()
