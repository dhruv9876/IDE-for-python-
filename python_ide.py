from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title('My Fantastic IDE')
compiler.geometry("800x600")

file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    global file_path
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    if path:
        with open(path, 'r') as file:
            code = file.read()
            editor.delete('1.0', END)
            editor.insert('1.0', code)
            set_file_path(path)

def save_file():
    global file_path
    if file_path == '':
        save_as()
    else:
        with open(file_path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)

def save_as():
    global file_path
    path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    if path:
        with open(path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            set_file_path(path)

def run():
    global file_path
    if file_path == '':
        save_prompt = Toplevel()
        Label(save_prompt, text='Please save your code first!').pack()
        Button(save_prompt, text="OK", command=save_prompt.destroy).pack()
        return

    process = subprocess.Popen(
        ['python', file_path],
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        shell=False
    )

    output, error = process.communicate()

    code_output.delete('1.0', END)
    code_output.insert(END, output.decode())
    code_output.insert(END, error.decode())

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=compiler.destroy)
menu_bar.add_cascade(label='File', menu=file_menu)

run_menu = Menu(menu_bar, tearoff=0)
run_menu.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_menu)

compiler.config(menu=menu_bar)

editor = Text(font=("Consolas", 12), wrap="none")
editor.pack(expand=True, fill=BOTH)

code_output = Text(height=10, font=("Consolas", 12), bg="#1e1e1e", fg="white")
code_output.pack(fill=BOTH)

compiler.mainloop()
