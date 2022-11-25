import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
score = 0
class UserIntreface():
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.root = tk.Tk()
        self.root.title("Quize App")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = tk.Label(text=f"Score: {score}", font=("Arial", 14, "normal"), bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.question_canvas = tk.Canvas(width=300, height=250, bg = "white")
        self.canvas_text = self.question_canvas.create_text(
            150, 125, 
            text= "",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=250,
        )
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)
        


        correct_image = tk.PhotoImage(file=r"images/true.png")
        self.correct_button = tk.Button(image=correct_image, command= lambda: self.get_answer("True"))
        self.correct_button.config(highlightthickness=0, bg=THEME_COLOR, bd=0)
        self.correct_button.grid(column=0, row=2)

        wrong_image = tk.PhotoImage(file=r"images/false.png")
        self.wrong_button = tk.Button(image=wrong_image, command= lambda: self.get_answer("False"))
        self.wrong_button.config(highlightthickness=0, bg=THEME_COLOR, bd=0)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        global score
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.canvas_text, text= q_text)
            

    def get_answer(self, user_answer):
        global score
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)
        

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.question_canvas.after(1000, self.get_next_question)