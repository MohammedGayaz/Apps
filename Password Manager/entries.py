import tkinter as tk

# all the necessary entries

email = []


def write_file():
    with open("userFiles/email_list.txt", mode='w') as f:
        f.write("example@mail.com")


try:
    open("userFiles/email_list.txt")
except FileNotFoundError:
    write_file()
else:
    with open("userFiles/email_list.txt") as f:
        if f.read() == "":
            write_file()

with open("userFiles/email_list.txt") as file:
    for x in file:
        email.append(x.strip())
    cont = file.read()


def configEntry(entry):
    entry.config(width=25, font=("Arial", 16))


class EntriesFields():
    def __init__(self, window):
        self.clicked = tk.StringVar(value='↓ Select')
        self.web_entry = tk.Entry(window)
        self.web_entry.focus()
        configEntry(self.web_entry)
        self.web_entry.grid(column=1, row=1, columnspan=2, pady=(50, 0), sticky="w")

        self.user_entry = tk.Entry(window)
        configEntry(self.user_entry)
        self.user_entry.grid(column=1, row=2, columnspan=2, sticky="w")

        self.email_entry = tk.Entry(window)
        self.email_entry.insert(tk.END, email[0])
        configEntry(self.email_entry)
        self.email_entry.grid(column=1, row=3, sticky="w")

        self.drop = tk.OptionMenu(window, self.clicked, *email, command=self.show)
        self.drop.config(highlightthickness=0)
        self.drop.grid(column=2, row=3)

        self.password_entry = tk.Entry(window)
        configEntry(self.password_entry)
        self.password_entry.grid(column=1, row=4, sticky="w")

    def show(self, choice):
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(tk.END, choice)
        self.clicked.set(value='↓ Select')

    def update_options(self, window):
        with open("userFiles/email_list.txt") as f:
            mail = []
            for x in f:
                mail.append(x.strip())
            print(mail)
            self.drop.destroy()
            self.drop = tk.OptionMenu(window, self.clicked, *mail, command=self.show)
            self.drop.config(highlightthickness=0)
            self.drop.grid(column=2, row=3)
