import tkinter as tk

calculation=""

def add_to_calculaion(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete('1.0', tk.END)
    text_result.insert(1.0, calculation)
def evaluate():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
    except:
        clear()
        text_result.insert(1.0, "Error")
def clear():
    global calculation
    calculation = ""
    text_result.delete('1.0', tk.END)
    text_result.insert(1.0, calculation)

root = tk.Tk()
root .geometry("400x600")
text_result = tk.Text(root, height=2, width=20, font=("Century Gothic", 30))
text_result.grid(row=0, columnspan=5)
root.mainloop()