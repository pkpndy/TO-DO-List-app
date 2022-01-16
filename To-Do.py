from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('MyDaily-ToDo List!')
root.geometry("500x500")

my_font = Font(family="Brush Script MT Italic", size=30, weight="bold")

my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame, font=my_font, width=25, height=5,
                  bg="SystemButtonFace", bd=0, fg="#464646", highlightthickness=0,
                  selectbackground="#a6a6a6", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)
# stuff = ["Do Exercise", "Anything"]

# for item in stuff:
#     my_list.insert(END, item)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

my_entry = Entry(root, font=("Helvetica", 24), width=26)
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)


def delete_item():
    my_list.delete(ANCHOR)
    pass


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)
    pass


def task_done():
    my_list.itemconfig(my_list.curselection(), fg="#dedede")
    my_list.select_clear(0, END)
    pass


def not_done():
    my_list.itemconfig(my_list.curselection(), fg="#464646")
    my_list.select_clear(0, END)
    pass


def delete_done():
    count = 0
    while(count < my_list.size()):
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1


def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Users/pkpnd/Desktop", title="Save File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
        # Delete items that are done before saving
        count = 0
        while(count < my_list.size()):
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count += 1

        stuff = my_list.get(0, END)
        # open the file
        output_file = open(file_name, 'wb')

        pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:/Users/pkpnd/Desktop", title="Save File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        my_list.delete(0, END)
        input_file = open(file_name, 'rb')
        stuff = pickle.load(input_file)
        for item in stuff:
            my_list.insert(END, item)


def delete_list():
    my_list.delete(0, END)


my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=delete_list)


delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
done_button = Button(button_frame, text="Task Done", command=task_done)
not_done_button = Button(button_frame, text="Not Done", command=not_done)
delete_done_button = Button(
    button_frame, text="Delete Done", command=delete_done)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
done_button.grid(row=0, column=2)
not_done_button.grid(row=0, column=3, padx=20)
delete_done_button.grid(row=0, column=4)


root.mainloop()
