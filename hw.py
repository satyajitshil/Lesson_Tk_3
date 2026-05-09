from tkinter import *

tk = Tk()
tk.title("Account Creator")
tk.geometry("800x500")

frame = Frame(master=tk,height=400, width=720, bg="#6ac2bc")

lbl_1=Label(frame, text="Principal",bg="#1d75f5",fg="#ffffff")
lbl_2=Label(frame, text="Rate",bg="#1d75f5",fg="#ffffff")
lbl_3=Label(frame, text="Time(Years)",bg="#1d75f5",fg="#ffffff")

princ_entry=Entry(frame)
rate_entry=Entry(frame)
time_entry=Entry(frame)

def display():
    principal = princ_entry.get()
    rate = rate_entry.get()
    time = rate_entry.get()
    compound = float(principal) * float(float(1+float(rate)/100)) ** float(time)
    simple = float(principal) * float(1+float(float(rate)/100)*float(time))
    com_message = "The total money you have now in compoud interest in "+str(time)+" year(s) with an interest rate of "+str(rate)+" is "+str(compound)+" (Principal = "+str(principal)+").\n"
    simp_message = "The total money you have now in simple interest in "+str(time)+" year(s) with an interest rate of "+str(rate)+" is "+str(simple)+" (Principal = "+str(principal)+").\n"
    

    text_box.insert(END, simp_message)
    text_box.insert(END, com_message)

text_box = Text(bg="#1d75f5",fg="#ffffff",height=10,width=100)
btn = Button(text="Calculate",command=display, bg="#1d75f5",fg="#000000" )

frame.place(x=20,y=0)
lbl_1.place(x=20,y=20)
princ_entry.place(x=150,y=20)
lbl_2.place(x=20,y=80)
rate_entry.place(x=150,y=80)
lbl_3.place(x=20,y=140)
time_entry.place(x=150,y=140)
btn.place(x=150,y=200)
text_box.place(x=20,y=240)

tk.mainloop()
