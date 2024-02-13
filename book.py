from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE
def new_file():
    global_name = "Без названия"
    text.delete('1.0', END)

def save():
        out = asksaveasfile(mode='w', defaultextension='.txt') #сохраняем в формат тхт
        data = text.get('1.0', END)
        try:
            out.write(data.rstrip())
        except Exception: # исключение
            messagebox.showerror("Файл не сохранить")
def open_file():
    global file_name
    input = askopenfile(mode='r')
    if input is None:
       return 
       file_name = input.name
       data = input.read()
       text.delete('1.0', END)
       text.insert('1.0', data)

root = Tk()
root.title("Заметки")
root.geometry("600x600") # добавляем текстовое поле
text = Text(root, width=600, height=600)
text.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)

file_menu.add_command(label="NEW", command=new_file)#добавляем функцию 
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="SaveFile", command=save)

menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)
root.mainloop()
