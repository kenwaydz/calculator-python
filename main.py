from tkinter import *
window =Tk()
result=0
currentOP=""
def add() :
    global result,currentOP
    num=float(output.get())
    result+=num
    output.delete(0,END)
    currentOP="add"
def click(num) :
    current=output.get()
    output.delete(0,END)
    output.insert(0,str(current)+str(num))
def clear() :
    global result
    result=0
    output.delete(0,END)
def equal() :
    global result,currentOP
    match currentOP :
        case "add" :
            result+=float(output.get())


    output.delete(0,END)
    output.insert(0,str(result))
    result=0
buttons= [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2)
]
window.title("Calculator")
window.geometry("430x550")
frame1=Frame(window)
frame1.pack(fill=X,expand=YES)

output=Entry(frame1,width=60,borderwidth=3)
output.grid(row=0,column=0,columnspan=4,padx=15,pady=15)

for button in buttons:

  Button(frame1,text=button[0],font=("arial",18),padx=35,pady=10,command=lambda num=button[0]: click(num)).grid(row=button[1],column=button[2])

buttonplus=Button(frame1,text="+",font=("arial",18),padx=32,pady=10,command=add).grid(row=1,column=3)
buttonminus=Button(frame1,text="-",font=("arial",18),padx=35,pady=10).grid(row=2,column=3)
buttonmultip=Button(frame1,text="*",font=("arial",18),padx=35,pady=10).grid(row=3,column=3)
button0=Button(frame1,text="0",font=("arial",18),padx=35,pady=10).grid(row=4,column=1)
buttonC=Button(frame1,text="C",font=("arial",18),padx=33,pady=10,command=clear).grid(row=4,column=2)
buttondiv=Button(frame1,text="/",font=("arial",18),padx=33,pady=10).grid(row=4,column=3)
buttonpoint=Button(frame1,text=".",font=("arial",18),padx=37,pady=10,command=lambda :click(".")).grid(row=4,column=0)
buttonequals=Button(frame1,text="=",font=("arial",18),padx=33,pady=10,command=equal).grid(row=4,column=3)




window.mainloop()
