from tkinter import Tk,Button,Listbox
from tkinter.constants import CENTER
import control_win

from add_category import Add_c_win
from add_word import Add_word

class Add_win():
    def __init__(self,root):
        control_win.main_win_created =True

        win = root

        win.protocol("WM_DELETE_WINDOW", self.on_closing)
        #use for close win
        self.win2 = win

        win.title("Add")
        win.geometry("400x400")
        win.minsize(width=400,height=400)
        win.maxsize(width=400,height=400)
        win.minsize(height=400,width=400)
        win.maxsize(height=400,width=400)
        #with double click list box will be update
        win.bind('<Double-Button-1>',lambda e: self.show_categories())

        btn_add_category = Button(win,text=" Add ",padx=20,pady=3,command=self.open_add_category_win)
        btn_del_category = Button(win,text=" Delete ",padx=15,pady=3,command=self.delete_category)
        btn_select_category = Button(win,text=" Select ",padx=20,pady=7,command=self.open_add_word_win)

        self.lbox_category = Listbox(win,width=63,height=18,justify=CENTER)
    
        btn_add_category.place(x=30,y=23)
        btn_del_category.place(x=290,y=23)
        btn_select_category.place(x=160,y=20)

        self.lbox_category.place(x=8,y=80)

        self.show_categories()

    def on_closing(self):
        control_win.main_win_created = False
        self.win2.destroy()

    def p(self):
        print("pppp")
        
    def open_add_category_win(self):
        if control_win.add_win_created == False:
            root = Tk()
            Add_c_win(root)
            

    def show_categories(self):
        self.data = control_win.get_categories()
        self.lbox_category.delete(0,'end')
        for i in self.data:
            self.lbox_category.insert('end',i[1])

    def delete_category(self):
        if self.lbox_category.curselection() :
            index = self.lbox_category.curselection()
            category = self.data[index[0]]
            id = category[0]
            control_win.delete_category_by_id(id)
            self.show_categories()
    
    def open_add_word_win(self):
        if control_win.add_win_created == False and self.lbox_category.curselection():
            index = self.lbox_category.curselection()
            category = self.data[index[0]]
            control_win.id_category = category[0]
            root = Tk()
            Add_word(root)








