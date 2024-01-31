from tkinter import *
def button_press(num):
    global equation_text
    equation_text=equation_text+str(num)
    equation_labels.set(equation_text)

def equals():
    global equation_text
    try:
       total=str(eval(equation_text))
       equation_labels.set(total)
       equation_text=total
    except ZeroDivisionError:
        equation_text.set("ERROR")
        equation_text=""
    except SyntaxError:
        equation_labels.set("SYNTAX ERROR")

def clear():
    global equation_text
    equation_labels.set("")
    equation_text=""


window =Tk()
window.title("CALCULATOR")
window.geometry("600x600")
equation_text=""


equation_labels=StringVar()
label =Label(window,textvariable=equation_labels,font=('consolas',20),bg="white",width=24,height=2)
label.pack()
frame=Frame(window)
frame.pack()
button1=Button(frame,text=1,height=4,width=9,font=35,
               command=lambda:button_press(1))
button1.grid(row=0,column=0)
button2=Button(frame,text=2,height=4,width=9,font=35,
               command=lambda:button_press(2))
button2.grid(row=0,column=1)
button3=Button(frame,text=3,height=4,width=9,font=35,
               command=lambda:button_press(3))
button3.grid(row=0,column=2)
button4=Button(frame,text=4,height=4,width=9,font=35,
               command=lambda:button_press(3))
button4.grid(row=1,column=0)
button5=Button(frame,text=5,height=4,width=9,font=35,
               command=lambda:button_press(5))
button5.grid(row=1,column=1)
button6=Button(frame,text=6,height=4,width=9,font=35,
               command=lambda:button_press(6))
button6.grid(row=1,column=2)
button7=Button(frame,text=7,height=4,width=9,font=35,
               command=lambda:button_press(7))
button7.grid(row=2,column=0)
button8=Button(frame,text=8,height=4,width=9,font=35,
               command=lambda:button_press(8))
button8.grid(row=2,column=1)
button9=Button(frame,text=9,height=4,width=9,font=35,
               command=lambda:button_press(9))
button9.grid(row=2,column=2)
button0=Button(frame,text=0,height=4,width=9,font=35,
               command=lambda:button_press(0))
button0.grid(row=3,column=0)
plus=Button(frame,text='+',height=4,width=9,font=35,
            command=lambda :button_press('+'))
plus.grid(row=0,column=3)
minus=Button(frame,text='-',height=4,width=9,font=35,
            command=lambda :button_press('-'))
minus.grid(row=1,column=3)
divide=Button(frame,text='/',height=4,width=9,font=35,
            command=lambda :button_press('/'))
divide.grid(row=2,column=3)
multiply=Button(frame,text='x',height=4,width=9,font=35,
            command=lambda :button_press('x'))
multiply.grid(row=3,column=3)
equals=Button(frame,text='=',height=4,width=9,font=35,
            command=equals)
equals.grid(row=3,column=2)
point=Button(frame,text='.',height=4,width=9,font=35,
            command=lambda :button_press('.'))
point.grid(row=3,column=1)
clear=Button(window,text='clear',height=4,width=39,font=35,
            command=clear)
clear.pack()


window.mainloop()
