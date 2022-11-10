import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
PINK = "#FF043E"
RED = "#FF5858"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
long_break_count = 0
short_break_count = 0
round_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global rep, round_count, long_break_count, short_break_count
    timer_canvas.itemconfig(timer_text, text="00:00")
    rep, round_count, long_break_count, short_break_count = 0, 0, 0, 0
    short_break_text(short_break_count=0)
    long_break_text(long_break_count=0)
    round_text(round_count=0)
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #

def round_text(round_count):
    round_lable.config(text=f"{round_count}/4")
    heading_canvas.itemconfig(heading_text, text="FOCUS")
    heading_canvas.config(background=RED, highlightthickness=0)
    timer_canvas.config(background=RED, highlightthickness=0)

def short_break_text(short_break_count):
    short_break_lable.config(text=f"{short_break_count}")
    heading_canvas.itemconfig(heading_text, text="SHORT BREAK")
    heading_canvas.config(background=GREEN,highlightthickness=0)
    timer_canvas.config(background=GREEN,highlightthickness=0)

def long_break_text(long_break_count):
    long_breal_lable.config(text=f"{long_break_count}")
    heading_canvas.itemconfig(heading_text, text="LONG BREAK")
    heading_canvas.config(background=GREEN, highlightthickness=0)
    timer_canvas.config(background=GREEN, highlightthickness=0)

def start_timer():
    global rep, long_break_count, short_break_count, round_count
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if rep == 7:
        count_down(long_break_sec)
        rep = 0
        long_break_count += 1
        long_break_text(long_break_count)
    elif rep % 2 == 0:
        count_down(work_sec)
        rep += 1
        if round_count == 4:
            round_count = 0
        round_count += 1
        round_text(round_count)
    else:
        count_down(short_break_sec)
        rep += 1
        short_break_count += 1
        short_break_text(short_break_count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    timer_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if rep % 2 != 0:
            start_timer()

# ---------------------------- UI SETUP ------------------------------- #



window = tk.Tk()
window.minsize(width=400, height=600)
window.maxsize(width=400, height=600)
window.title("Pomodoro")


TASK_COORD = (60, 50)
SHORT_BREAK_COORD = (200, 50)
LONG_BREAK_COORD = (330, 50)


#heading canvas
heading_canvas = tk.Canvas(width=400, height=100, bd=-2)
heading_canvas.config(background=RED)
heading_text = heading_canvas.create_text(200, 80, text="TIMER", fill=YELLOW, font=(FONT_NAME, 30,"normal"))
heading_canvas.grid(column=0, row=0)


#main center timer text
timer_canvas = tk.Canvas(width=400, height= 400, bd = -2)
timer_canvas.config(background=RED)
timer_text = timer_canvas.create_text(200, 150, text="00:00", fill="white", font=(FONT_NAME, 60,"bold"))


start_button = tk.Button(timer_canvas, text="Start", font=(FONT_NAME, 14, "normal"), command=start_timer)
start_button.config(padx=156, background=GREEN)
start_button.place(x=10, y=300)

stop_button = tk.Button(timer_canvas, text="Stop", font=(FONT_NAME, 14, "normal"), command=reset_timer)
stop_button.config(padx=161, background=PINK)
stop_button.place(x=10, y= 350)

timer_canvas.grid(column=0, row=1)


# bottom score record
canvas = tk.Canvas(width=400, height=100, highlightthickness=0)
canvas.config(background=YELLOW)

canvas.create_text(60, 20, text="ROUND",fill="black")
round_lable = tk.Label(canvas, text="0/4", background=YELLOW, font=(FONT_NAME, 30, "normal"))
round_lable.place(x=30, y = 40)

canvas.create_text(200, 20, text="SHORT BREAK", fill="black")
short_break_lable = tk.Label(canvas, text="0", background=YELLOW, font=(FONT_NAME, 40, "normal"))
short_break_lable.place(x=180, y=30)

canvas.create_text(320, 20, text="LONG BREAK")
long_breal_lable = tk.Label(canvas, text="0", background=YELLOW, font=(FONT_NAME, 40, "normal"))
long_breal_lable.place(x=300, y=30)
canvas.grid(column=0, row=2)



window.mainloop()