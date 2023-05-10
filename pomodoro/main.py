from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
WORK_SESSIONS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS, WORK_SESSIONS, TIMER
    REPS = 0
    WORK_SESSIONS = 0
    window.after_cancel(TIMER)
    title.config(text="Timer")
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS, WORK_SESSIONS
    REPS += 1
    checkmark_text = "✔" * WORK_SESSIONS
    checkmark.config(text=checkmark_text)
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_time)
        title.config(fg=RED, text="Long break")
    elif REPS % 2 == 1:
        WORK_SESSIONS += 1
        count_down(work_time)
        title.config(fg=GREEN, text="Work")
    else:
        count_down(short_break_time)
        title.config(fg=PINK, text="Short break")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global TIMER
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=2)

title = Label()
title.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
title.grid(row=0, column=2)

start = Button()
start.config(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button()
reset.config(text="Reset", command=reset_timer)
reset.grid(row=2, column=4)

checkmark = Label()
checkmark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark.grid(row=3, column=2)

window.mainloop()
