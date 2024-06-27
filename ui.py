import time

THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class UiInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lable = Label(text="Score:0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "italic"))
        self.score_lable.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, rows=1, columnspan=2, pady=50)

        right_img = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.check_true)
        self.right_button.grid(column=0, row=2, padx=10)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.check_false)
        self.false_button.grid(column=1, row=2, padx=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_lable.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
