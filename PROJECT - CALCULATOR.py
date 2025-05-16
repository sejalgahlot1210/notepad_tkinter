from tkinter import *
import ast
 
root = Tk()

#prints number on entry widget when the button is clicked
i = 0
def get_number(num):
    #when you declare a variable outside of the function 
    #you are unable to access it
    #for this the global variable is used
    global i
    display.insert(i,num)
    i += 1

display = Entry(root)
display.grid(row=1, columnspan=6)

#prints operator on entry widget when button is clicked
def get_operator(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i += length

def clear_entry():
    display.delete(0, END)

def calculate():
    entire_string = display.get()
    #AST: Abstract Syntax Tree module 
    try:
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node,'<string>','eval'))
        clear_entry()
        display.insert(0,result)
    except Exception:
        clear_entry()
        display.insert(0,"Error")

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_entry()
        display.insert(0,new_string)
    else:
        clear_entry()
        display.insert(0,"")


#for the get_number funcion to know which number is clicked
#we create an array of numbers
numbers = [1,2,3,4,5,6,7,8,9]
counter = 0
for i in range(3):
    for j in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text,width=4, height=3, command= lambda text=button_text :get_number(text)) 
        button.grid(row=i+2,column=j,padx=3,pady=3)
        counter += 1
button = Button(root, text='0',width=4, height=3, command= lambda : get_number(0))
button.grid(row=5, column=1,padx=3,pady=3)

Button(root, text="Clear", width=4,height=3, command=clear_entry).grid(row=5, column=0,padx=3, pady= 3)
Button(root, text="=", width=4,height=3, command=calculate).grid(row=5, column=2,padx=3, pady= 3)
Button(root, text="<-", width=4,height=3,command=lambda: undo()).grid(row=5, column=4,padx=3, pady= 3)

count = 0
operations = ['+','-','*','/','*3.14','%','(','**',')','**2']
for i in range(4):
    for j in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count],width=4, height=3, command= lambda text=operations[count]: get_operator(text))
            count += 1
            button.grid(row=i+2,column=j+3,padx=3,pady=3)
       
root.mainloop()