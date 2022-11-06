import tkinter as tk
from tkinter import filedialog, ttk

from main import generate_adjacency_matrix

root = tk.Tk()
root.title('Adjacency Matrix Generator')
root.resizable(False, False)
root.geometry('300x150')

input_file = ""


def select_file():
    global input_file
    filetypes = (
        ('Excel files', ['*.xlsx', '*.xls']),
    )
    filename = filedialog.askopenfilename(
        title='Open a file',
        filetypes=filetypes)
    if filename:
        status.set("File read complete")
        input_file = filename
        save_button["state"] = tk.ACTIVE


def save_file():
    global input_file
    filetypes = (
        ('Excel files', ['*.xlsx', '*.xls']),
    )
    filename = filedialog.asksaveasfilename(
        title='Save to file',
        filetypes=filetypes)
    if filename:
        status.set("Generating matrix...")
        generate_adjacency_matrix(input_file, filename)
        status.set("Matrix saved")


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)
open_button.pack(expand=True)

status = tk.StringVar()
status.set("Waiting for file...")
status_label = ttk.Label(root, textvariable=status)
status_label.place(x=40, y=60)

# save button
save_button = ttk.Button(
    root,
    text='Save to File',
    state=tk.DISABLED,
    command=save_file
)
save_button.pack(expand=True)

# run the application
root.mainloop()
