from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

tk = Tk()
tk.geometry("800x800")
tk.title("Codingal Text Editor")

tk.rowconfigure(0,minsize=800,weight=1)
tk.columnconfigure(1,minsize=800,weight=1)



def open_file():
    filepath = askopenfilename(
	filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
	)
    if not filepath:
		    
        return
    text_edit.delete(1.0,END)
    with open(filepath,"r") as input_file:
        text= input_file.read()

        text_edit.insert(END, text)
        input_file.close()
    tk.title(f"Codingal's Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension="txt",
                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    if not filepath:
		    
        return

    with open(filepath,"w") as output_file:
        text = text_edit.get(1.0,END)
        output_file.write(text)
    tk.title(f"Codingal's Text Editor - {filepath}")

text_edit = Text(tk)
fr_buttons = Frame(tk, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

# Start the GUI event loop
tk.mainloop()
