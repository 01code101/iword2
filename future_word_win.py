from tkinter import Label,Entry,Button,Listbox
import control_win


class Future_word():
    def __init__(self,root):
        
        control_win.win_show = True
        win = root
        self.win2 = win
        win.title("Future Word")
        win.geometry("280x100")
        win.minsize(width=280,height=100)
        win.maxsize(width=280,height=100)
        win.protocol("WM_DELETE_WINDOW", self.on_closing)

        lbl_word= Label(win,text="WORD :")
        self.entry_word = Entry(win,width=40)
        btn_confirm = Button(win,text="add",command=self.click)

        lbl_word.place(x=18,y=7)
        self.entry_word.place(x=20,y=32)
        btn_confirm.place(x=120,y=60)
    
    def click(self):
        word = self.entry_word.get()
        if word != '':
            control_win.insert_future_word(word)
            self.entry_word.delete(0,'end')

    def on_closing(self):
        control_win.win_show = False
        self.win2.destroy()
    

class Future_word_list():
    def __init__(self,root,data):
        
        win = root
        win.title("Future Word")
        win.geometry("220x210")

        self.lb_future_word = Listbox(win,width=29,height=10,font = "Calibri 10")
        btn_delete = Button(win,text="delete",width=10,command=self.click1)

        self.lb_future_word.place(x=7,y=5)
        btn_delete.place(x=68,y=175)
        self.update_data(data)

    
    def click1(self):
        if self.lb_future_word.curselection():
            word = self.lb_future_word.get(self.lb_future_word.curselection())
            control_win.delete_future_word(word)
            self.lb_future_word.delete(self.lb_future_word.curselection())

    def update_data(self,data):
        for i in data:
            self.lb_future_word.insert('end',i[0])
