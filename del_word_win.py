from tkinter import Entry,Button,Listbox,Frame,Label
from tkinter.constants import FALSE, W
from typing import Text
import control_win

class Delete_word():
    def __init__(self,root):
        control_win.main_win_created =True

        win = root

        self.win2 = win
        win.protocol("WM_DELETE_WINDOW", self.on_closing)

        win.title("Delete Word")
        win.geometry("600x370")
        win.minsize(width=600,height=370)
        win.maxsize(width=600,height=370)

        self.txt_search_word = Entry(win,width=50)
        btn_search = Button(win,text=">",padx=4,pady=1,command= self.search_word)
        btn_delete = Button(win,text=" Delete ",pady=4,padx=22,background="orange")

        lbox_word = Listbox(win,width=45,height=18,border=2)
        lbox_word.insert(0,"joy")
        lbox_word.insert(1,"respect")
        lbox_word.insert(2,"hill")

        frame1 = Frame(win,width=260,height=292)

        lbl_category = Label(frame1,text="Category: 400")
        lbl_date = Label(frame1,text="Add Date: 2021/1/14")
        lbl_level = Label(frame1,text="Level: 2")
        lbl_review = Label(frame1,text="Number of review: 34")

        self.txt_search_word.place(x=50,y=20)
        btn_search.place(x=370,y=16)
        btn_delete.place(x=460,y=12)

        lbox_word.place(x=30,y=60)
        frame1.place(x=310,y=60)

        lbl_category.place(x=20,y=10)
        lbl_date.place(x=20,y=40)
        lbl_level.place(x=20,y=70)
        lbl_review.place(x=20,y=100)

    def on_closing(self):
        control_win.main_win_created = False
        self.win2.destroy()

