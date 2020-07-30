from tkinter import *

window = Tk()
window.title('Calculator')
window.iconbitmap('D:/python projects/MINI-PROJECTS/calculator/calculator.ico')

display = Entry(window,bd=48,insertwidth=4,font=('calibri',21,'bold'),bg='#d9d2ff')
display.grid(row=0,column=0,columnspan=4,padx=8)

def display_input(number):
    current = display.get()
    display.delete(0,END)
    display.insert(0,str(current)+ str(number))

def display_clear():
    display.delete(0,END)
    
def display_addition():
    global f_num
    global calculate
    calculate ='add'
    first_number = display.get()
    f_num=int(first_number)
    display.delete(0,END)

def display_subtraction():
    global f_num
    global calculate
    calculate ='sub'
    first_number = display.get()
    f_num=int(first_number)
    display.delete(0,END)

def display_multiplication():
    global f_num
    global calculate
    calculate ='mul'
    first_number = display.get()
    f_num=int(first_number)
    display.delete(0,END)

def display_division():
    global f_num
    global calculate
    calculate ='div'
    first_number = display.get()
    f_num=int(first_number)
    display.delete(0,END)

def display_modulus():
    global f_num
    global calculate
    calculate ='mod'
    first_number = display.get()
    f_num=int(first_number)
    display.delete(0,END)    

    
def display_equalsto():
    second_number = display.get()
    display.delete(0,END)
    
    if(calculate =='add'):
        display.insert(0,f_num + int(second_number))
        
    if(calculate=='sub'):
        display.insert(0,f_num - int(second_number))
        
    if(calculate=='mul'):
        display.insert(0,f_num * int(second_number))
        
    if(calculate=='div'):
        display.insert(0,f_num / int(second_number))
        
    if(calculate=='mod'):
        display.insert(0,f_num % int(second_number))
    
    
    

    
button1 = Button(window,text='1',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=lambda:display_input(1))
button2 = Button(window,text='2',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=lambda:display_input(2))
button3 = Button(window,text='3',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=lambda:display_input(3))
button4 = Button(window,text='4',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=lambda:display_input(4))
button5 = Button(window,text='5',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=lambda:display_input(5))
button6 = Button(window,text='6',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=lambda:display_input(6))
button7 = Button(window,text='7',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=lambda:display_input(7))
button8 = Button(window,text='8',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=lambda:display_input(8))
button9 = Button(window,text='9',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=lambda:display_input(9))
button0 = Button(window,text='0',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=lambda:display_input(0))

button_clear = Button(window,text='clear',padx=107,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=display_clear)
button_equalto = Button(window,text='=',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=display_equalsto)
button_addition = Button(window,text='+',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=display_addition)
button_subtraction = Button(window,text='-',padx=22,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=display_subtraction)
button_multiplication = Button(window,text='*',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=display_multiplication)
button_division = Button(window,text='/',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=display_division)
button_modulus = Button(window,text='%',padx=20,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=display_modulus)
button_decimal = Button(window,text='.',padx=23,bd=8,bg='#d9d2ff',font=('calibri',20,'bold'),command=display_input)





button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
button_decimal.grid(row=4,column=1)
button_modulus.grid(row=4,column=2)

button_clear.grid(row=5,column=0,columnspan=3)
button_equalto.grid(row=5,column=3)
button_addition.grid(row=3,column=3)

button_subtraction.grid(row=2,column=3)
button_multiplication.grid(row=1,column=3)
button_division.grid(row=4,column=3)









window.mainloop()
