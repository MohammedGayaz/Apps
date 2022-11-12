import tkinter as tk
# all the necessary labels

UI_BG = "#E1E5EA"
FONT_BG = "#181D31"

class LableName():
    def __init__(self, window):
        self.web_label = tk.Label(window, text="Website: ")
        self.label_config(self.web_label)
        self.web_label.grid(column=0, row=1, pady=(50, 0))

        self.user_name = tk.Label(window, text="User Name: ")
        self.label_config(self.user_name)
        self.user_name.grid(column=0, row=2)

        self.email_label = tk.Label(window, text="Email: ")
        self.label_config(self.email_label)
        self.email_label.grid(column=0, row=3)

        self.password_label = tk.Label(window, text="Password: ")
        self.label_config(self.password_label)
        self.password_label.grid(column=0, row=4)
        


    def label_config(self, label):
        label.config(bg=UI_BG, fg=FONT_BG, font=("Arial", 16, "normal"),
                    pady=10, padx=30, anchor="e", width=10)


