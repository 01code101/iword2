from tkinter import Button,Frame,Canvas, Label, Toplevel
from add_win import Add_win
from review_win import Review_win
from del_word_win import Delete_word
from gold_win import Gold_win
import control_win
from settings import start



class Main_win():
    def __init__(self,root):
        global review_num
        review_num = int()
        win = root
        win.title("iWord2")
        win.geometry("600x400")
        win.minsize(height=400,width=600)
        win.maxsize(height=400,width=600)

        self.canvas = Canvas(win,width=600,height=300)

        f_d = Frame(win,background="#74bdd4",height=100,width=600)
        self.btn_add = Button(f_d,text="ADD",padx=28,pady=6,command = self.open_add_win)
        btn_review = Button(f_d,text="REVIEW",padx=40,pady=15,command = self.open_review_win)
        self.btn_delete = Button(f_d,text="DELETE",padx=25,pady=6,command = self.open_delete_win)
        ####new changes 2022/4/6
        btn_gold = Button(f_d,text="Review Gold",padx=15,pady=-1,command = self.open_gold_win)

        f_s = Frame(win,width=600,height=200)
        self.lbl_all_words = Label(f_s,font = "Calibri 18",foreground="blue")
        self.lbl_gold_words = Label(f_s,font = "Calibri 12",foreground="#2E86C1")
        self.lbl_wating_words = Label(f_s,font = "Calibri 12",foreground="#2E86C1")

        f_d.place(x=0,y=300)
        
        btn_review.place(x=240,y=15)
        btn_gold.place(x=253,y=73)


        f_s.place(x=0,y=0)
        self.lbl_all_words.place(y=12,x=270)
        self.lbl_gold_words.place(y=50,x=17)
        self.lbl_wating_words.place(y=50,x=435)
        
        self.show_statistics()
        self.settings()
        #self.canvas.place(x=0,y=0)


        
    def open_add_win(self):
        if control_win.main_win_created == False:
            root = Toplevel()
            Add_win(root)
            root.mainloop()
            self.show_statistics()

    def open_review_win(self):
        if control_win.main_win_created == False:
            self.update_libox()
            root = Toplevel()
            Review_win(root)
            root.mainloop()
            self.show_statistics()

    def open_delete_win(self):
        if control_win.main_win_created == False:
            root = Toplevel()
            Delete_word(root)
            root.mainloop()
            self.show_statistics()

    def open_gold_win(self):
        if control_win.gold_win_created == False:
            root = Toplevel()
            Gold_win(root)
            root.mainloop()

    def update_libox(self):
        global review_num
        num_of_records_in_libox = control_win.count_libox_records() 
        
        if num_of_records_in_libox < review_num:
            data = control_win.select_words_id_for_libbox()
            for i in data:
                if num_of_records_in_libox < review_num:
                    control_win.insert_word_to_libox(i[0])
                    control_win.update_state_T_word(i[0])
                    #num_of_records_in_libox = control_win.count_libox_records() 
                    num_of_records_in_libox = num_of_records_in_libox + 1
                    self.show_statistics()

    def show_statistics(self):
        data = control_win.data_for_statistics()
        self.lbl_all_words.config(text=str(data[0]))
        self.lbl_gold_words.config(text="GOLD WORDS: "+str(data[1]))
        self.lbl_wating_words.config(text="WATING WORDS: "+str(data[2]))

    def settings(self):
        global review_num
        data = start(False)
        review_num = int(data[0])
        
        print(str(data[1]).lower().strip())

        if(str(data[1]).lower().strip() == "yes" ):
            self.reset_database()
            start(True)
        
        if(str(data[2]).lower().strip() == "off"):
            self.btn_add.place(x=30,y=33)
            self.btn_delete.place(x=475,y=33)
        



    def reset_database(self):
        control_win.reset_database()