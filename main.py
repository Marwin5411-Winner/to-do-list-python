from tkinter import *
from tkinter import ttk


status = "Not Done"

def add():
    print("Add button clicked")
    print("Entry: ", taskEntry.get())
    listbox.insert(END, taskEntry.get())
    taskEntry.delete(0, END)

def delete():
    print("Delete button clicked")
    print("Entry: ", listbox.curselection()[0])
    listbox.delete(listbox.curselection()[0])

def mark():
    print("Mark button clicked")
    print("Entry: ", listbox.curselection()[0])
    listbox.itemconfig(listbox.curselection()[0], fg="gray")

def save():
    print("Save button clicked")
    f=open("todo.txt", "w")
    for i in range(listbox.size()):
        f.write(listbox.get(i)+"\n")
    f.close()


def load():
    print("Load button clicked")
    f=open("todo.txt", "r")
    for line in f:
        listbox.insert(END, line)
    f.close()

def select(event):
    print("Listbox clicked")
    print("Entry: ", listbox.curselection()[0])
    if listbox.itemcget(listbox.curselection()[0], "fg") == "gray":
        statusLabel.config(text="Done")
    else:
        statusLabel.config(text="Not Done")



root = Tk()
root.title("To Do List")
root.geometry("400x300")
root.resizable(False, False)



frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Todo list").grid(column=0, row=0)
statusLabel=ttk.Label(frm, text=status, relief=SUNKEN)
statusLabel.grid(column=1, row=2)
listbox=Listbox(frm, height=5, width=15)
listbox.grid(column=0, row=2)

listbox.bind('<<ListboxSelect>>', select)


taskEntry=ttk.Entry(frm)
taskEntry.grid(column=0, row=1)

addBtn=ttk.Button(frm, text="Add", command=add).grid(column=1, row=1)
deleteBtn=ttk.Button(frm, text="Delete", command=delete).grid(column=0, row=4)
markBtn=ttk.Button(frm, text="Mark Done", command=mark).grid(column=1, row=4)
saveBtn=ttk.Button(frm, text="Save", command=save).grid(column=0, row=5)
loadBtn=ttk.Button(frm, text="Load", command=load).grid(column=1, row=5)


root.mainloop()




