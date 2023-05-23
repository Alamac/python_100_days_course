from tkinter import Tk, Canvas, Button, Label, PhotoImage, messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.q_text = self.canvas.create_text(150, 125, text="Sample Question", font=FONT, fill=THEME_COLOR, width=280)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)


        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            command=lambda:
            self.check_answer("True")
        )
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            command=lambda: self.check_answer("False")
        )
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q)
        else:
            self.finish_game()

    def check_answer(self, answer: str):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def finish_game(self):
        messagebox.showinfo(title="Game over!", message=f"Your final score is {self.quiz.score}! Congrats!")
        self.window.destroy()
