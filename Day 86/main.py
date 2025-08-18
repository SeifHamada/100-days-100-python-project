from tkinter import *
from datetime import datetime


window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20)

start_time = None


def start_test():
    global start_time

    start_time = datetime.now()
    user_try.delete("1.0", "end")
    user_try.config(state="normal")
    result.config(text="")


def measure_speed(event):
    global start_time

    typed_text = user_try.get("1.0", "end-1c").strip()
    target_text = text_paragraph.cget("text").strip()

    if typed_text == target_text:
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds() / 60
        word_count = len(typed_text.split())
        wpm = word_count / duration
        result.config(text=f"Your speed is {wpm:.2f} WPM")
        user_try.config(state="disabled")


text_paragraph = Label(text="Some people combine touch typing and hunt and peck by using a buffering method."
                       " In the buffer method, the typist looks at the source copy,"
                       " mentally stores one or several sentences,"
                       " then looks at the keyboard and types out the buffer of sentences."
                       " This eliminates frequent up and down motions with the head and is used in typing competitions in which the typist is not well versed in touch typing."
                       " Not normally used in day-to-day contact with keyboards,"
                       " this buffer method is used only when time is of the essence.", wraplength=500, justify="left")
text_paragraph.grid(column=0, row=0, columnspan=2, pady=10)

user_try = Text(width=60, height=10, state="disabled")
user_try.bind("<KeyRelease>", measure_speed)
user_try.grid(column=0, row=1, columnspan=2, pady=10)

start_button = Button(text="Start", command=start_test)
start_button.grid(column=0, row=2, pady=10)

result = Label(text="", font=("Arial", 12, "bold"))
result.grid(column=0, row=3, columnspan=2, pady=2)

window.mainloop()
