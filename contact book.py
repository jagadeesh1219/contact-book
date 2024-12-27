from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('700x550')
root.config(bg='#d3f3f5')
root.title('Contact Book')
root.resizable(0, 0)
contactlist = [
    ['John Doe', '1234567890'],
    ['Jane Smith', '0987654321']
]
Name = StringVar()
Number = StringVar()
def add_contact():
    contactlist.append([Name.get(), Number.get()])
    update_listbox()

def edit_contact():
    selected_contact = listbox.curselection()
    contactlist[selected_contact[0]] = [Name.get(), Number.get()]
    update_listbox()

def delete_contact():
    selected_contact = listbox.curselection()
    del contactlist[selected_contact[0]]
    update_listbox()

def update_listbox():
    listbox.delete(0, END)
    for contact in contactlist:
        listbox.insert(END, contact)
frame = Frame(root)
frame.pack(pady=20)

listbox = Listbox(frame, width=50, height=10)
listbox.pack(side=LEFT, padx=20)

scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)

entry_name = Entry(root, textvariable=Name)
entry_name.pack(pady=5)
entry_number = Entry(root, textvariable=Number)
entry_number.pack(pady=5)

button_add = Button(root, text="Add Contact", command=add_contact)
button_add.pack(pady=5)
button_edit = Button(root, text="Edit Contact", command=edit_contact)
button_edit.pack(pady=5)
button_delete = Button(root, text="Delete Contact", command=delete_contact)
button_delete.pack(pady=5)
update_listbox()
root.mainloop()
