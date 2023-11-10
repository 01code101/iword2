from tkinter import Tk,Button,Entry,Frame,Label,Text,StringVar
from tkinter import ttk
from tkinter.constants import END
from future_word_win import Future_word_list
import pyperclip

import control_win
class Add_word():
    def __init__(self,root):
        win = root
        win.title("Add Word")
        win.geometry("500x460")
        win.minsize(width=500,height=460)
        win.maxsize(width=500,height=460)

        #create widget______________________________________________________
        self.lbl_word = Label(win,text="Word :")
        self.txt_word = Entry(win,width=33)

        self.lbl_role = Label(win,text="Role :")
        values = ('verb','noun','adjective','adverb','other')
        sv = StringVar()
        self.cb_role = ttk.Combobox(win,textvariable=sv,width=30)
        self.cb_role['values'] = values
        self.cb_role['state'] = 'readonly'
        self.cb_role.bind('<<ComboboxSelected>>',lambda e: self.set_noraml())

        sv1 = StringVar()
        values = ('normal','fast')
        self.cb_type = ttk.Combobox(win,textvariable=sv1,width=30)
        self.cb_type['values'] = values
        self.cb_type['state'] = 'readonly'
        self.cb_type.current(0)

        self.lbl_type = Label(win,text="Review_type :")
        

        f1 = Frame(win,width=480,height=270)
        self.lbl_app1 = Label(f1,text="Application1 :")
        lbl_app2 = Label(f1,text="Application2 :")
        lbl_app3 = Label(f1,text="Application3 :")

        self.txt_app1 = Entry(f1,width=60,state='disable')
        self.txt_app2 = Entry(f1,width=60,state='disable')
        self.txt_app3 = Entry(f1,width=60,state='disable')

        self.txt_example_app1 = Text(f1,width=45,height=3)
        self.txt_example_app1.tag_add('warning',index1='end')
        self.txt_example_app1.tag_config("warning", foreground="red")

        self.txt_example_app2 = Text(f1,width=45,height=3,state="disabled")
        self.txt_example_app3 = Text(f1,width=45,height=3,state='disabled')

        self.txt_example_app1.bind("<Control-v>",lambda e: self.ctrl_v(e))
        self.txt_example_app2.bind("<Control-v>",lambda e: self.ctrl_v(e))
        self.txt_example_app3.bind("<Control-v>",lambda e: self.ctrl_v(e))

        self.lbl_verb = Label(win,text="Verb :")
        self.txt_verb = Entry(win,width=33,border=3,state="disabled")

        btn_summit = Button(win,text="Summit",padx=40,pady=7,border=4,command=self.insert_word_to_db)
        #place widget in win____________________________________________
        self.lbl_word.place(x=120,y=10)
        self.txt_word.place(x=170,y=10)

        self.lbl_role.place(x=120,y=40)
        self.cb_role.place(x=170,y=40)

        self.lbl_type.place(x=80,y=67)
        self.cb_type.place(x=170,y=67)

        f1.place(x=10,y=90)

        self.lbl_app1.place(x=10,y=10)
        self.txt_app1.place(x=99,y=10)
        self.txt_example_app1.place(x=99,y=35)
        

        lbl_app2.place(x=10,y=97)
        self.txt_app2.place(x=99,y=97)
        self.txt_example_app2.place(x=99,y=122)

        lbl_app3.place(x=10,y=184)
        self.txt_app3.place(x=99,y=184)
        self.txt_example_app3.place(x=99,y=209)

        self.lbl_verb.place(x=120,y=370)
        self.txt_verb.place(x=165,y=370)

        btn_summit.place(x=180,y=405)

        self.check_future_words()

    def check_future_words(self):
        data = control_win.select_all_future_word()
        
        if data :
            root = Tk()
            Future_word_list(root,data)
            root.mainloop()
    

    def ctrl_v(self,e):
        clipboard = pyperclip.paste()
        index = clipboard.find("*")
        data = ""
        if index == -1:
            data = clipboard + '*'
        else:
            data = clipboard.replace('*','')
            data = data + "*"
        pyperclip.copy(data)
        

    def insert_word_to_db(self):
        data = [0,'',0,'','','','','','','',0]

        word = self.txt_word.get()
        word  = word.replace(" ", "")
        index = self.cb_role.current() + 1
        verb = self.txt_verb.get()
        apps = [self.txt_app1.get(),self.txt_app2.get(),self.txt_app3.get()]
        examples = [self.txt_example_app1.get("1.0",'end-1c'),self.txt_example_app2.get("1.0",'end-1c'),self.txt_example_app3.get("1.0",'end-1c')]
        
        if word != ''  and index != 0:
            if examples[0].find('\nput * at end of each sentences') != -1:
                examples[0] =  examples[0].replace("\nput * at end of each sentences","")
            str = examples[0]
            star  = str.find("*")
            
            if star != -1:
                if index == 1 and verb != '' and apps[0] != '' :
                    data[0] = control_win.id_category
                    data[1] = word
                    data[2] = index
                    data[3] = apps[0]
                    data[6] = examples[0]
                    if apps[1] != '':
                        data[4] = apps[1]
                        data[7] = examples[1]
                    else:
                        data[4] = ''
                        data[7] = ''
                    if apps[2] != '':
                        data[5] = apps[2]
                        data[8] = examples[2]
                    else:
                        data[5] = ''
                        data[8] = ''
                    data[9] = ''
                    data[10] = self.cb_type.current() + 1
                    print(data)
                    newdata = [0,'','','','']
                    data_verb = verb.split('*')
                    if len(data_verb) == 4:
                        control_win.insert_word_to_db(data)
                        newdata[1] = data_verb[0]
                        newdata[2] = data_verb[1]
                        newdata[3] = data_verb[2]
                        newdata[4] = data_verb[3]
                        control_win.insert_verb_to_db(newdata)
                        self.clear_txt()
                    else:
                        if verb.find("      enter 5 verb split with *") == -1:
                            self.txt_verb.insert('end',"      enter 5 verb split with *",)

                else:
                    if verb == '' and index == 1:
                        self.lbl_verb.config(foreground="red")
                    else:
                        self.lbl_verb.config(foreground="black")
                    if apps[0] == '' and index == 1: 
                        self.lbl_app1.config(foreground="red")
                    else:
                        self.lbl_app1.config(foreground="black")

                if index != 1 and examples[0] != '':
                    data[0] = control_win.id_category
                    data[1] = word
                    data[2] = index
                    data[9] = examples[0]
                    data[10] = self.cb_type.current() + 1
                    print(data)
                    control_win.insert_word_to_db(data)
                    self.clear_txt()
            else:
                self.txt_example_app1.insert('end','\nput * at end of each sentences','warning')
        else:
            if word == '':
                self.lbl_word.config(foreground="red")
            else:
                self.lbl_word.config(foreground="black")
            if index == 0:
                self.lbl_role.config(foreground="red")
            else:
                self.lbl_role.config(foreground="black")

    #category_id = data[0]
        #word = data[1]
        #role = data[2]
        #app1 = data[3]
        #app2 = data[4]
        #app3 = data[5]
        #examples_app1 = data[6]
        #examples_app2 = data[7]
        #examples_app3 = data[8]
        #examples = data[9]

    def set_noraml(self):
        index = self.cb_role.current() + 1
        if index  == 1:
            self.txt_verb.config(state='normal')
            self.txt_app1.config(state='normal')
            self.txt_app2.config(state='normal')
            self.txt_app3.config(state='normal')
            self.txt_example_app2.config(state='normal')
            self.txt_example_app3.config(state='normal')
        else:
            self.txt_verb.config(state='disable')
            self.txt_app1.config(state='disable')
            self.txt_app2.config(state='disable')
            self.txt_app2.config(state='disable')
            self.txt_example_app2.config(state='disable')
            self.txt_example_app3.config(state='disable')

    def clear_txt(self):
        self.txt_word.delete(0,'end')
        self.txt_app1.delete(0,'end')
        self.txt_app2.delete(0,'end')
        self.txt_app3.delete(0,'end')
        self.txt_verb.delete(0,'end')
        self.txt_example_app1.delete("1.0",'end')
        self.txt_example_app2.delete("1.0",'end')
        self.txt_example_app3.delete("1.0",'end')
        self.cb_role.set('')




