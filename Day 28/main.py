from tkinter import *
import math

reps = 0
timer = None

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

def start():
    global reps
    reps += 1

    work_second = 25 * 60
    short_break_second = 5 * 60
    long_break_second = 20 * 60

    if reps % 8 == 0:
        countdown(long_break_second)
        title_label.config(text="Break", fg="#e7305b")
    elif reps % 2 == 0:
        countdown(short_break_second)
        title_label.config(text="Break", fg="#e2979c")
    else:
        countdown(work_second)
        title_label.config(text="Work", fg="#9bdeac")

def countdown(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#f7f5dd")

title_label = Label(text="Timer", fg="#9bdeac", bg="#f7f5dd", font=("Courier", 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check = Label(fg="#9bdeac", bg="#f7f5dd")
check.grid(column=1, row=3)

window.mainloop()
