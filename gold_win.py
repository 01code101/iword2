from tkinter import Button, Label
import control_win



class Gold_win():
    def __init__(self,root):

        control_win.gold_win_created =True
        self.current_word=0
        self.all_gold_words = list() 
        self.word_num = 0

        win = root
        win.title("Gold Words")
        win.geometry("600x400")
        win.minsize(height=400,width=500)
        win.maxsize(height=400,width=500)

        win.protocol("WM_DELETE_WINDOW", self.on_closing)
        #use for close win
        self.win2 = win

        btn_next = Button (win,text=" > ",padx=5,pady=3,command = self.show_next_word)
        btn_former = Button (win,text=" < ",padx=5,pady=3,command = self.show_former_word)

        self.lbl_gold_word = Label (win,font = "Calibri 24",foreground="blue")

        btn_next.place(x=454,y=181)
        btn_former.place(x=10,y=181)
        self.lbl_gold_word.place(x=214,y=20)

        self.all_golds()

    def on_closing(self):
        control_win.gold_win_created = False
        self.win2.destroy()

        
    def show_next_word(self):
        if(self.current_word < self.word_num):
            self.current_word = self.current_word + 1
            self.lbl_gold_word.config(text=str(self.all_gold_words[self.current_word][0]))

    def show_former_word(self):
        if(self.current_word > 0):
            self.current_word = self.current_word - 1
            self.lbl_gold_word.config(text=str(self.all_gold_words[self.current_word][0]))

    def all_golds(self):
        self.all_gold_words = control_win.select_all_gold_words()
        self.word_num = len(self.all_gold_words)-1
        self.lbl_gold_word.config(text=str(self.all_gold_words[self.current_word][0]))
        