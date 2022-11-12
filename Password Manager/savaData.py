import tkinter as tk
from tkinter import messagebox
import json




def conformation(website, email_data, password_data):
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: "
                f"\nEmail: {email_data} "
                f"\nPassword: {password_data} \nIs it ok to save?")

    return is_ok


def get_data(window, entry_fields):
    website = entry_fields.web_entry.get()
    email_data = entry_fields.email_entry.get()
    with open("userFiles/email_list.txt", mode="r") as f:
        email = []
        for mail in f:
            email.append(mail.strip())
    # print(email)
    if email_data not in email:
        email.append(email_data)
        with open("userFiles/email_list.txt", mode="a") as f:
            f.write(f"\n{email_data}")
        entry_fields.update_options(window)
    user = entry_fields.user_entry.get()
    password_data = entry_fields.password_entry.get()

    if len(website) == 0 or len(password_data) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any fields empty."
        )
    else:
        is_ok = conformation(website, email_data, password_data)
        if is_ok:
            new_data = {
                website:
                    {
                        "name": user,
                        "email": email_data,
                        "password": password_data
                    }
            }
            return new_data


def empty_fields(entry_fields):
    entry_fields.web_entry.delete(0, tk.END)
    entry_fields.user_entry.delete(0, tk.END)
    entry_fields.password_entry.delete(0, tk.END)


def open_new_file(new_data, entry_fields):
    with open("userFiles/data.json", mode='w') as f:
        json.dump(new_data, f, indent=4)
        print("file does not exist")
        empty_fields(entry_fields)


def add_data(window, entry_fields):
    new_data = get_data(window, entry_fields)
    try:
        with open("userFiles/data.json", mode='r') as f:
            data = json.load(f)
            print(data)
            if data is None:
                open_new_file(new_data, entry_fields)
    except FileNotFoundError:
        open_new_file(new_data, entry_fields)
    except ValueError:
        open_new_file(new_data, entry_fields)
    else:
        try:
            data.update(new_data)
        except (TypeError, AttributeError):
            empty_fields(entry_fields)
        else:
            with open("userFiles/data.json", mode='w') as f:
                json.dump(data, f, indent=4)
                empty_fields(entry_fields)
