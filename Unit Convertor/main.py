import tkinter as tk


window = tk.Tk()
window.title("convertor")
window.config(padx=25, pady=25)


def convert():
    global previous_km, previous_mile
    if previous_km == km_input.get():
        # convet miles to km
        km_input.delete(first=0, last=len(km_input.get()))
        mile = float(mile_input.get())
        km = mile * 1.609
        km_input.insert(0, string=f"{km}")

    elif previous_mile == mile_input.get():
        # convert km to miles
        mile_input.delete(first=0, last=len(mile_input.get()))
        km = float(km_input.get())
        mile = km / 1.609
        mile_input.insert(0, string=f"{round(mile, 4)}")


    previous_km = km_input.get()
    previous_mile = mile_input.get()

previous_km, previous_mile = "0", "0"


title_lable = tk.Label(text="Units convertor", font = ("Arial", 20, "bold"))
title_lable.config(pady=20)
title_lable.grid(column=1, row=0)


km_lable = tk.Label(text="Km:", font = ("Arial", 16, "normal"))
km_lable.config(pady=20)
km_lable.grid(column=0, row=1)

km_input = tk.Entry()
km_input.insert(0, "0")
km_input.grid(column=1, row=1)

mile_lable = tk.Label(text="Miles:", font = ("Arial", 16, "normal"))
mile_lable.config(pady=20)
mile_lable.grid(column=0, row=2)

mile_input = tk.Entry()
mile_input.insert(0, "0")
mile_input.grid(column=1,row=2)

button = tk.Button(text="Convert", width=10, command=convert)
button.config(padx=25, font = ("Arial", 10, "bold"))
button.grid(column=1, row=3,)
window.mainloop()