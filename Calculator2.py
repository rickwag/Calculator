import tkinter as tk

class Calculator:

    def __init__(self):
        self.win = tk.Tk()
        self.expression = tk.StringVar()
        self.expression.set("0")

        self.AddWidgets()

    def ToScreen(self, text):
        text = str(text)
        if self.expression.get() == "0":
            self.expression.set(text)
        else:
            self.expression.set(self.expression.get() + text)

    def ClearScreen(self):
        self.expression.set("0")

    def CalculateAnswer(self,event = None):
        try:
            self.expression.set(eval(self.expression.get()))
        except:
            self.expression.set("Error")

    def AddWidgets(self):
        self.MainFrame = tk.LabelFrame(self.win,
                                       text="Calculator",
                                       foreground = "green",
                                       font = ("Ariel", 32, "bold"))
        self.MainFrame.grid(row = 0,
                            column = 0,
                            padx = 10,
                            pady = 10)
        self.MainEntry = tk.Entry(self.MainFrame,
                                  textvariable=self.expression,
                                  font = ("Ariel",32,"italic"))
        self.MainEntry.grid(row=0,
                            columnspan=4,
                            padx=5,
                            pady=5,
                            sticky=tk.E)

        self.button0 = tk.Button(self.MainFrame,
                                 text="0",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command=lambda: self.ToScreen(0))
        self.button1 = tk.Button(self.MainFrame,
                                 text="1",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command=lambda: self.ToScreen(1))
        self.button2 = tk.Button(self.MainFrame,
                                 text="2",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command=lambda: self.ToScreen(2))
        self.button3 = tk.Button(self.MainFrame,
                                 text="3",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command=lambda: self.ToScreen(3))
        self.button4 = tk.Button(self.MainFrame,
                                 text="4",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command=lambda: self.ToScreen(4))
        self.button5 = tk.Button(self.MainFrame,
                                 text="5",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command=lambda: self.ToScreen(5))
        self.button6 = tk.Button(self.MainFrame,
                                 text="6",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command=lambda: self.ToScreen(6))
        self.button7 = tk.Button(self.MainFrame,
                                 text="7",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command=lambda: self.ToScreen(7))
        self.button8 = tk.Button(self.MainFrame,
                                 text="8",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command=lambda: self.ToScreen(8))
        self.button9 = tk.Button(self.MainFrame,
                                 text="9",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command=lambda: self.ToScreen(9))
        row = 1
        column = 0
        for button in self.MainFrame.winfo_children()[1:]:
            if column < 3:
                button.grid(row=row,
                            column=column,
                            padx=5,
                            pady=5)
                column += 1
            else:
                row += 1
                column = 0
                button.grid(row=row,
                            column=column,
                            padx=5,
                            pady=5)
                column += 1

        self.plusButton = tk.Button(self.MainFrame,
                                      text="+",
                                      width=8,
                                      foreground="dark blue",
                                      background="green",
                                      relief=tk.RAISED,
                                      bd=8,
                                      font=("ariel", 20, "italic"),
                                      command=lambda :self.ToScreen("+"))
        self.plusButton.grid(row=row,#where it ended
                             column=column, #where it ended
                             padx=5,
                             pady=5)
        self.minusButton = tk.Button(self.MainFrame,
                                 text="-",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command = lambda :self.ToScreen("-"))
        self.minusButton.grid(row = row,
                              column = column+1,
                              padx=5,
                              pady=5)
        self.timesButton = tk.Button(self.MainFrame,
                                 text="*",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command = lambda :self.ToScreen("*"))
        self.timesButton.grid(row=row+1,
                              column=0,
                              padx=5,
                              pady=5)
        self.divideButton = tk.Button(self.MainFrame,
                                 text="/",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command = lambda :self.ToScreen("/"))
        self.divideButton.grid(row=row+1,
                               column=1,
                               padx=5,
                               pady=5)
        self.openBracketButton = tk.Button(self.MainFrame,
                                 text="(",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command = lambda :self.ToScreen("("))
        self.openBracketButton.grid(row=row+2,
                                    column=0,
                                    padx=5,
                                    pady=5)
        self.closeBracketButton = tk.Button(self.MainFrame,
                                 text=")",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command = lambda :self.ToScreen(")"))
        self.closeBracketButton.grid(row=row+2,
                                     column=1,
                                     padx=5,
                                     pady=5)

        self.clearButton = tk.Button(self.MainFrame,
                                 text="cls",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command = self.ClearScreen)
        self.clearButton.grid(row=row+1,
                              column=2,
                              padx=5,
                              pady=5)
        self.equalsButton = tk.Button(self.MainFrame,
                                 text="=",
                                 width=8,
                                 foreground="dark blue",
                                 background="green",
                                 relief=tk.RAISED,
                                 bd=8,
                                 font=("ariel", 20, "italic"),
                                 command = self.CalculateAnswer)
        self.equalsButton.grid(row=row+2,
                               column=2,
                               padx=5,
                               pady=5)
        #bind when focus is on whole window not specific button
        self.win.bind("<Return>", self.CalculateAnswer)

calc = Calculator()
calc.win.mainloop()