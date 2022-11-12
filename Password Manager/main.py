import tkinter as tk


from labels import LableName
from entries import EntriesFields
from genPassword import passwordGen
from webSearch import TableData, data_table
import savaData


def generated_password():
    password = passwordGen()
    all_entries.password_entry.delete(first=0, last=tk.END)
    all_entries.password_entry.insert(tk.END, password)


def save_data():
    savaData.add_data(window, all_entries)


def table():
    df = data_table()
    table_data = TableData(df)


UI_BG = "#E1E5EA"
FONT_BG = "#181D31"

window = tk.Tk()
window.title("Password Manager")
window.iconbitmap(r'images/logo.ico')
window.grid_columnconfigure(2, weight=1)
window.geometry("700x500")
window.maxsize(width=700, height=500)
window.config(bg=UI_BG, padx=50)

# top heading and logo
head_canvas = tk.Canvas(width=400, height=100)
image_lock = tk.PhotoImage(file=r'images/lock.png')
head_canvas.create_image(50, 75, image=image_lock)
head_canvas.create_text(230, 75, text="Password Manager",
                        font=("Times new roman", 30, "normal"), fill=FONT_BG)
head_canvas.config(background=UI_BG, highlightthickness=0)
head_canvas.grid(column=0, row=0, columnspan=3)

all_labels = LableName(window)
all_entries = EntriesFields(window)

search_button = tk.Button(text='Search', width=10, command=table)
search_button.grid(column=2, row=1, pady=(50, 0))

generate_button = tk.Button(text="Generate", width=10, command=generated_password)
generate_button.grid(column=2, row=4)

add_button = tk.Button(text="SAVE", width=35, font=("Arial", 10, "bold"), command=save_data)
add_button.grid(column=1, row=6, columnspan=3, pady=(20, 20), sticky="w")

window.mainloop()
