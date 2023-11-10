
from tkinter import Entry,Button,Label,Frame, Listbox,PhotoImage,Toplevel
from tkinter.constants import CENTER, FALSE, LEFT
import control_win
import pyttsx3
from threading import Thread
import future_word_win 
import random

class Review_win():
    global all_word
    all_word = 0

    global current_word
    current_word = 0

    global word
    word = ""

    global data_libox
    data_libox = list()

    global full_word
    full_word = list()

    global f_word_show
    f_word_show = False


    def __init__(self,root):
        control_win.main_win_created =True
        global f_word_show
        f_word_show = False
        win = root

        win.protocol("WM_DELETE_WINDOW", self.on_closing)
        #use for close win
        self.win2 = win

        win.title("Review")
        win.geometry("700x500")
        win.minsize(width=700,height=500)
        win.maxsize(width=700,height=500)

        #image for speaker
        speaker_photo = PhotoImage(file= r"src\speaker.png")
        self.img = speaker_photo.subsample(4,6)

        #frame spell-----------------------------------
        self.f_spell = Frame(win,width=640,height=440)

        #show current word and all word
        self.lbl_word_all = Label(self.f_spell,font = "Calibri 12")
        self.lbl_word_all.config(text="  0 / 0 ")
        self.lbl_word_all.place(x=290,y=15)
        
        #show a clickable speaker icon
        lbl_pronounce = Label(self.f_spell,image=self.img)
        lbl_pronounce.place(x=160,y=64)
        #this code make lbl_pronounce a cilckable label
        lbl_pronounce.bind("<Button-1>",lambda e:self.check_engine())
        
        #get spell of a word
        self.txt_word = Entry(self.f_spell,width=20,bd=5,justify=CENTER,font = "Calibri 20",fg="Green")
        self.txt_word.place(x=175,y=320)

        #this code return all pressed button of keyboard
        #first e is part of syntax,but second e is part of code func
        win.bind("<Key>",lambda e: self.f(e))

        

        #frame yes and no -----------------------------
        self.f_y_n = Frame(win,width=650,height=430)
        
        self.lbl_word = Label(self.f_y_n,font = "Calibri 14")
        self.lbl_role = Label(self.f_y_n,font = "Calibri 10")

        self.lbl_p1 = Label(self.f_y_n,text=" O ",foreground="green")
        self.lbl_p2 = Label(self.f_y_n,text=" O ",foreground="blue")
        self.lbl_p3 = Label(self.f_y_n,text=" O ",foreground="red")

        self.lbl_example1 = Label(self.f_y_n,font = "Calibri 12",justify=LEFT)
        self.lbl_example2 = Label(self.f_y_n,font = "Calibri 12",justify=LEFT)
        self.lbl_example3 = Label(self.f_y_n,font = "Calibri 12",justify=LEFT)

        self.btn_yes = Button(self.f_y_n,text=" Yes ",padx=17,pady=10,font = "Calibri 15",background="green",command=self.yes)
        self.btn_No = Button(self.f_y_n,text=" No ",padx=17,pady=10,font = "Calibri 15",background="purple",command=self.no)

        self.lbl_word.place(x=290,y=0)
        self.lbl_role.place(x=295,y=30)

        self.lbl_p1.place(x=0,y=62)


        self.lbl_example1.place(x=15,y=60)


        self.btn_yes.place(x=500,y=360)
        self.btn_No.place(x=80,y=360)

        #frame f_words
        self.f_f_word = Frame(win,width=660,height=480,background='blue')
        self.lbox_f_word = Listbox(self.f_f_word,width=64,height=4,font = "Calibri 14")
        self.lbox_f_word.bind('<<ListboxSelect>>',lambda e: self.show_word())
        self.f_lbl = Frame(self.f_f_word,width=620,height=353)
        self.lbl_full_word = Label(self.f_lbl,font = "Calibri 12",justify=LEFT)
        self.lbl_word_and_role = Label(self.f_lbl,font = "Calibri 10",justify=CENTER)

        self.get_libox_data()
        self.init_f_spell()

#self is a necessary arg but it is null,e is main arg
    global past_input
    past_input = ''
    def f(self,e):
        global f_word_show
        global past_input
        if e.keysym == "Return" and f_word_show == False:
            self.check_word_spell()
        
        if e.keysym == 'Control_L':
            past_input = e.keysym
        
        if e.keysym == 'f' and past_input=='Control_L' :
            past_input = ''
            if self.f_y_n.winfo_ismapped() == 1 and control_win.win_show == False:
                root = Toplevel()
                future_word_win.Future_word(root)
                root.mainloop()
        
        

    global v
    v = False
    def pronounce_word(self,word):
        global v
        print('**********sdfadf*a*sdf**asdf')
        engine = pyttsx3.init()
        print('after')
        v = engine.getProperty(name='voice')
        engine.setProperty('rate', 90)
        
        # this line added recently
        voices = engine.getProperty('voices')
        
        if v == False:
            # engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
            engine.setProperty('voice', voices[0].id)
            v= True
        else:
            # engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
            engine.setProperty('voice', voices[1].id)
            v = False
        
        engine.say(word)
        engine.runAndWait() 
        engine.stop()

    def on_closing(self):
        control_win.main_win_created = FALSE

        global all_word
        all_word = 0
        global current_word
        current_word = 0
        global word
        word = ""
        global data_libox
        data_libox = list()
        global full_word
        full_word = list()
        

        self.win2.destroy()

    def get_libox_data(self):
        global data_libox
        data_libox = control_win.select_libox_id()


#################################################################f_spell
    def init_f_spell(self):
        self.f_y_n.place_forget()
        self.f_spell.place(x=30,y=30)

        global data_libox
        global current_word
        global word
        global full_word
        global all_word
        global t
        all_word = len(data_libox)

        if all_word != 0:
            self.lbl_word_all.config(text=f"{current_word + 1}"+" / "+f"{all_word}")
            full_word = self.get_word_by_id(data_libox[current_word][0])
            word = full_word[0][0]

            
            t = Thread(target=self.pronounce_word,args=(word,))
            t.start()
        else:
            t = Thread(target=self.pronounce_word,args=('no word',))
            t.start()
        


    def get_word_by_id(self,id):
        word = control_win.select_word_by_id(id)
        return word

    def check_word_spell(self):
        user_word = self.txt_word.get().lower()
        if user_word == "-end":
            self.show_f_word_frame()
            return
        global word
        global current_word
        global all_word
        global t
        global data_libox
        global f_word

        
        if user_word == word.lower() and word != '':
            self.init_f_y_n()
        else:
            if t.is_alive() == False:
                if data_libox != [] :
                    id = data_libox[current_word][0]
                    next_level = 0
                    control_win.update_libox(id,next_level)
                    f_word.append(full_word)
                if current_word + 1 < all_word:
                    current_word += 1
                    self.txt_word.delete(0,'end')
                    self.init_f_spell()
                else:
                    self.f_y_n.place_forget()
                    self.f_spell.place_forget()
                    self.show_f_word_frame()

    def check_engine(self):
        # if t.isAlive() == False:  
        if t.is_alive() == False:
            self.pronounce_word(word)
    
    def init_f_y_n(self):
        values = ('verb','noun','adjective','adverb','other')
        self.f_spell.place_forget()
        self.f_y_n.place(x=25,y=35)
        self.lbl_example1.config(text='')
        self.lbl_example2.config(text='')
        self.lbl_example3.config(text='')

        global full_word
        self.lbl_word.config(text=full_word[0][0])
        self.lbl_role.config(text=values[full_word[0][1] - 1])
        if full_word[0][8] != '':
            self.lbl_example2.place_forget()
            self.lbl_example3.place_forget()
            self.lbl_p2.place_forget()
            self.lbl_p3.place_forget()

            ex = full_word[0][8]
            examples = ex.split('*')
            txt = ''
            for e in examples:
                txt = txt + e + '\n'
            txt = txt.strip()
            self.lbl_example1.config(text=txt)
        else:
            self.lbl_p2.place(x=0,y=152)
            self.lbl_p3.place(x=0,y=242)
            self.lbl_example2.place(x=15,y=150)
            self.lbl_example3.place(x=15,y=240)
            ex = full_word[0][5]
            examples = ex.split('*')
            examples.pop()
            txt = ''
            if 4 < len(examples):
                choosed = random.sample(examples, 4)
            else:
                choosed = examples
            for e in choosed:
                txt = txt + e + '\n'
            txt = txt.strip()
            self.lbl_example1.config(text=txt)
            #print(self.lbl_example1.)

            ex = full_word[0][6]
            examples = ex.split('*')
            examples.pop()
            txt = ''
            if 4 < len(examples):
                choosed = random.sample(examples, 4)
            else:
                choosed = examples
            for e in choosed:
                txt = txt + e + '\n'
            txt = txt.strip()
            self.lbl_example2.config(text=txt)

            ex = full_word[0][7]
            examples = ex.split('*')
            examples.pop()
            txt = ''
            if 4 < len(examples):
                choosed = random.sample(examples, 4)
            else:
                choosed = examples
            for e in choosed:
                txt = txt + e + '\n'
            txt = txt.strip()
            self.lbl_example3.config(text=txt)
    
    global f_word 
    f_word = list()

    def yes(self):
        global data_libox
        global current_word
        id = data_libox[current_word][0]
        next_level = data_libox[current_word][1] + 1
        word_type = control_win.get_word_type(id)

        if word_type[0][0] == 1:
            if next_level == 6 :
                control_win.set_word_gold(id)
            else:
                control_win.update_libox(id,next_level)
        else:
            if next_level == 4 :
                control_win.set_word_gold(id)
            else:
                control_win.update_libox(id,next_level)
        
        if current_word + 1 < all_word:
            current_word += 1
            self.txt_word.delete(0,'end')
            self.init_f_spell()
        else:
            self.f_y_n.place_forget()
            self.f_spell.place_forget()
            self.show_f_word_frame()

    
    def no(self):
        global data_libox
        global current_word
        id = data_libox[current_word][0]
        next_level = 0
        control_win.update_libox(id,next_level)

        f_word.append(full_word)
        if current_word + 1 < all_word:
            current_word += 1
            self.txt_word.delete(0,'end')
            self.init_f_spell()
        else:
            self.f_y_n.place_forget()
            self.f_spell.place_forget()
            self.show_f_word_frame()

    def show_f_word_frame(self):
        global f_word_show
        f_word_show = True
        global f_word
        for i in f_word:
            self.lbox_f_word.insert('end',i[0][0])
        
        self.f_f_word.place(x=20,y=10)
        self.lbox_f_word.place(x=7,y=10)
        self.f_lbl.place(x=20,y=117)
        self.lbl_word_and_role.place(x=270,y=0)
        self.lbl_full_word.place(x=0,y=25)

    def show_word(self):
        global f_word
        index = self.lbox_f_word.curselection()
        word = f_word[index[0]]
        values = ('verb','noun','adjective','adverb','other')
        lbl = ''
        lbl_w_r = ''

        if word[0][8] == '':
            id = control_win.get_id_by_name(word[0][0])
            verb_forms = control_win.get_verb_forms(id[0][0])
            examples1 = word[0][5].split('*')
            examples1.pop()
            examples2 = word[0][6].split('*')
            examples2.pop()
            examples3 = word[0][7].split('*')
            examples3.pop()

            if 4 < len(examples1):
                choosed1 = random.sample(examples1, 4)
            else:
                choosed1 = examples1
            if 4 < len(examples2):
                choosed2 = random.sample(examples2, 4)
            else:
                choosed2 = examples2
            if 4 < len(examples3):
                choosed3 = random.sample(examples3, 4)
            else:
                choosed3 = examples3
            
            lbl_w_r = '-' +word[0][0]+'-' + '\n' + values[0]
            self.lbl_word_and_role.config(text=lbl_w_r)
            ##################
            lbl = word[0][2]  + ' :'
            txt = ""
            for i in choosed1:
                txt = txt  + '   '+ i + '\n'
            txt = txt.strip()
            txt = '   ' + txt
            lbl = lbl + '\n' + txt + '\n'
            ##################
            lbl =  lbl + word[0][3] + ' :' + '\n'
            txt = ""
            for i in choosed2:
                txt = txt  +'   '+ i + '\n'
            txt = txt.strip()
            txt = '   ' + txt
            lbl = lbl  + txt + '\n'
            ##################
            lbl =  lbl + word[0][4]+ ' :' 
            txt = ""
            for i in choosed3:
                txt = txt + '   '+ i + '\n'
            txt = txt.strip()
            txt = '   ' + txt
            lbl = lbl + '\n' + txt
            ################
            lbl = lbl + '\n\n'
            lbl = lbl + '\t\t' + verb_forms[0][0]
            lbl = lbl + '\t' + verb_forms[0][1]
            lbl = lbl + '\t' + verb_forms[0][2]
            lbl = lbl + '\t' + verb_forms[0][3]

        else:
            examples1 = word[0][8].split('*')
            examples1.pop()
            lbl_w_r = '-' +word[0][0]+'-' + '\n' + values[word[0][1] -1]
            self.lbl_word_and_role.config(text=lbl_w_r)
            txt=''
            for i in examples1:
                txt = txt  + '   '+ i + '\n'
            txt = txt.strip()
            txt = '   ' + txt
            lbl = lbl + '\n' + txt + '\n'
        
        self.lbl_full_word.config(text= lbl)