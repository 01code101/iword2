from tkinter import Tk,Frame,Label,Listbox
from tkinter.constants import END


class Fword():
    def __init__(self,root):
        win = root
        win.title("Fword")
        win.geometry("600x520")
        win.minsize(width=600,height=520)
        win.maxsize(width=600,height=520)

        frame1 =Frame(win,width=570,height=180,background="red")

        lbox_fword = Listbox(frame1,width=92,height=10,border=3)

        frame = Frame(win,height=302,width=570,background="blue")

        lbl_word = Label(frame,text="big")
        lbl_rule = Label(frame,text="noune")

        lbl_application1 = Label(frame,text="application 1:")
        lbl_application2 = Label(frame,text="application 2:")
        lbl_application3 = Label(frame,text="application 3:")

        lbl_example_app1 = Label(frame,text="example 1\nexample 2\nexample 3")
        lbl_example_app2 = Label(frame,text="example 1\nexample 2\nexample 3")
        lbl_example_app3 = Label(frame,text="example 1\nexample 2\nexample 3")

        frame1.place(x=15,y=20)
        lbox_fword.place(x=5,y=5)
        for i in range(100):
            lbox_fword.insert(END,i)
        
        frame.place(x=15,y=210)

        lbl_word.place(x=270,y=10)
        lbl_rule.place(x=260,y=34)
        lbl_application1.place(x=10,y=60)
        lbl_example_app1.place(x=40,y=85)
        lbl_application2.place(x=10,y=140)
        lbl_example_app2.place(x=40,y=165)
        lbl_application3.place(x=10,y=220)
        lbl_example_app3.place(x=40,y=243)

        




root = Tk()
f1 = Fword(root)
root.mainloop()