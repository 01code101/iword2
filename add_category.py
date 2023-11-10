from tkinter import Button,Label,Entry,Text
import control_win

class Add_c_win():
    def __init__(self,root):
        control_win.add_win_created = True

        win = root
        win.title("Category")
        win.geometry("300x300")
        win.minsize(height=300,width=300)
        win.maxsize(height=300,width=300)

        win.protocol("WM_DELETE_WINDOW", self.on_closing)
        #use for close win
        self.win2 = win

        self.lbl_name = Label(win,text="Name: ")
        lbl_description = Label(win,text="Description: ")

        self.txt_name = Entry(win,width=34)
        self.txt_description = Text(win,width=22,height=10)

        btn_create = Button(win,text=" Create ",padx=10,pady=2,command=self.insert_data_to_db)

        self.lbl_name.place(x=30,y=20)
        self.txt_name.place(x=75,y=20)

        lbl_description.place(x=30,y=60)
        self.txt_description.place(x=105,y=60)

        btn_create.place(x=125,y=250)

    def on_closing(self):
        control_win.add_win_created = False
        self.win2.destroy()

    def insert_data_to_db(self):
        data = []

        if self.txt_name.get() != '' and self.txt_name.get() != 'enter the name':
            self.lbl_name.config(foreground='black')
            if self.txt_description.get("1.0",'end-1c') != '':
                data = [self.txt_name.get(),self.txt_description.get("1.0",'end-1c')]
            else:
                data = [self.txt_name.get(),'']
            control_win.insert_category_to_db(data)
            self.txt_name.delete(0,'end')
            self.txt_description.delete("1.0",'end')
            
        else:
            self.lbl_name.config(foreground='red')
            self.txt_name.delete(0,'end')
            self.txt_name.insert(0,'enter the name')
            

