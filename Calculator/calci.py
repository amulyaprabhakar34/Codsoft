import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        
        self.result_var = tk.StringVar()
        
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=("Helvetica", 20))
        self.result_entry.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)  # Clear button
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 15))
            button.grid(row=row, column=col, sticky="nsew")
            button.bind("<Button-1>", self.button_click)
        
        # Make the buttons expand to fill the grid cells
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        
        self.current_input = ""
    
    def button_click(self, event):
        clicked_text = event.widget.cget("text")
        
        if clicked_text == "=":
            try:
                result = str(eval(self.current_input))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
            self.current_input = ""
        elif clicked_text == "C":
            self.current_input = ""
            self.result_var.set("")
        else:
            self.current_input += clicked_text
            self.result_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
