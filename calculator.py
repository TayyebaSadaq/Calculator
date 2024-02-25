import tkinter as tk

calculation=""

def add_to_calculation(symbol):
    global calculation 
    calculation += str(symbol) # add the value of symbol to calculation
    text_result.delete('1.0', tk.END) # delete the current value of the text box
    text_result.insert(1.0, calculation) # insert the value of calculation into the text box

def evaluate():
    global calculation
    try: # try to evaluate the calculation
        calculation = str(eval(calculation)) # if successful, set result to the value of the calculation
        text_result.delete(1.0, "end") # delete the current value of the text box
        text_result.insert(1.0, calculation) # insert the value of result into the text box  
        calculation = ""
    except:
        clear()
        text_result.insert(1.0, "Error")# if unsuccessful, display error

def clear():
    global calculation
    calculation = ""
    text_result.delete('1.0', tk.END)
    text_result.insert(1.0, calculation)

root = tk.Tk()
root .geometry("400x600")

text_result = tk.Text(root, height=2, width=20, font=("Century Gothic", 30))
text_result.grid(row=0, columnspan=5)

# create buttons for nunmbers
btn1 = tk.Button(root, text="1", font=("Century Gothic", 30), command=lambda: add_to_calculation(1))
btn1.grid(row=1, column=0)
btn2 = tk.Button(root, text="2", font=("Century Gothic", 30), command=lambda: add_to_calculation(2))
btn2.grid(row=1, column=1)
btn3 = tk.Button(root, text="3", font=("Century Gothic", 30), command=lambda: add_to_calculation(3))
btn3.grid(row=1, column=2)
btn4 = tk.Button(root, text="4", font=("Century Gothic", 30), command=lambda: add_to_calculation(4))
btn4.grid(row=2, column=0)
btn5 = tk.Button(root, text="5", font=("Century Gothic", 30), command=lambda: add_to_calculation(5))
btn5.grid(row=2, column=1)
btn6 = tk.Button(root, text="6", font=("Century Gothic", 30), command=lambda: add_to_calculation(6))
btn6.grid(row=2, column=2)
btn7 = tk.Button(root, text="7", font=("Century Gothic", 30), command=lambda: add_to_calculation(7))
btn7.grid(row=3, column=0)
btn8 = tk.Button(root, text="8", font=("Century Gothic", 30), command=lambda: add_to_calculation(8))
btn8.grid(row=3, column=1)
btn9 = tk.Button(root, text="9", font=("Century Gothic", 30), command=lambda: add_to_calculation(9))
btn9.grid(row=3, column=2)
btn0 = tk.Button(root, text="0", font=("Century Gothic", 30), command=lambda: add_to_calculation(0))
btn0.grid(row=4, column=1)
btn_open = tk.Button(root, text="(", font=("Century Gothic", 30), command=lambda: add_to_calculation("("))
btn_open.grid(row=4, column=0)
btn_close = tk.Button(root, text=")", font=("Century Gothic", 30), command=lambda: add_to_calculation(")"))
btn_close.grid(row=4, column=2)

# create buttons for operations
btn_plus = tk.Button(root, text="+", font=("Century Gothic", 30), command=lambda: add_to_calculation("+"))
btn_plus.grid(row=1, column=3)
btn_minus = tk.Button(root, text="-", font=("Century Gothic", 30), command=lambda: add_to_calculation("-"))
btn_minus.grid(row=2, column=3)
btn_multiply = tk.Button(root, text="*", font=("Century Gothic", 30), command=lambda: add_to_calculation("*"))
btn_multiply.grid(row=3, column=3)
btn_divide = tk.Button(root, text="/", font=("Century Gothic", 30), command=lambda: add_to_calculation("/"))
btn_divide.grid(row=4, column=3)
btn_clear = tk.Button(root, text="C", font=("Century Gothic", 30), command=clear)
btn_clear.grid(row=5, column=1)
btn_equals = tk.Button(root, text="=", font=("Century Gothic", 30), command=evaluate)
btn_equals.grid(row=5, column=2)

root.mainloop()