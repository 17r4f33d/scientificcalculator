from tkinter import *
import sys

last_clicked = None


class CalcButton(Button):
	def __init__(self, symbol, **kwargs):
		super().__init__(**kwargs)
		self.symbol = symbol
		self.is_clicked = False


def remove_buttons(*buttons):
	for button in buttons:
		button.grid_remove()


def trigger_action(button):
	global last_clicked
	if last_clicked is calc_button_equal:
		last_clicked = button
		calc_display.delete(0, len(calc_display.get()))
	button.is_clicked = not button.is_clicked
	calc_display.insert(calc_display.index(INSERT), button.symbol)


def shift_buttons(shift_button):
	shift_button.is_clicked = not shift_button.is_clicked
	if shift_button.is_clicked:
		remove_buttons(calc_button_log, calc_button_sin, calc_button_cos, calc_button_tan, calc_button_parentheses_open)
		calc_button_ln.grid(row=1, column=1)
		calc_button_arcsin.grid(row=1, column=3)
		calc_button_arccos.grid(row=1, column=5)
		calc_button_arctan.grid(row=1, column=7)
		calc_button_parentheses_close.grid(row=2, column=9)
	else:
		remove_buttons(calc_button_ln, calc_button_arcsin, calc_button_arccos, calc_button_arctan, calc_button_parentheses_close)
		calc_button_log.grid(row=1, column=1)
		calc_button_sin.grid(row=1, column=3)
		calc_button_cos.grid(row=1, column=5)
		calc_button_tan.grid(row=1, column=7)
		calc_button_parentheses_open.grid(row=2, column=9)


calc_window = Tk()
calc_window.title("Scientific Calculator")
calc_display = Entry(width=50, borderwidth=10, relief=RIDGE, fg="White", bg="Black")
calc_display.grid(row=0, column=0, columnspan=11, padx=5, pady=5)
calc_button_log = CalcButton("Log", text="Log", width=5, relief=RAISED, fg="Black", bg="White", command=lambda: sys.exit())
calc_button_ln = CalcButton("Ln", text="Ln", width=5, relief=RAISED, fg="White", bg="Black")
calc_button_log.grid(row=1, column=1)
calc_button_sin = CalcButton("Sin", text="Sin", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_arcsin = CalcButton("ArcSin", text="Sin\u207B\u2071", width=5, relief=RAISED, fg="White", bg="Black")
calc_button_sin.grid(row=1, column=3)
calc_button_cos = CalcButton("Cos", text="Cos", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_arccos = CalcButton("ArcCos", text="Cos\u207B\u2071", width=5, relief=RAISED, fg="White", bg="Black")
calc_button_cos.grid(row=1, column=5)
calc_button_tan = CalcButton("Tan", text="Tan", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_arctan = CalcButton("ArcTan", text="Tan\u207B\u2071", width=5, relief=RAISED, fg="White", bg="Black")
calc_button_tan.grid(row=1, column=7)
calc_button_shift = CalcButton("Shift", text="Shift", width=5, relief=RAISED, fg="Black", bg="White", command=lambda: shift_buttons(calc_button_shift))
calc_button_shift.grid(row=1, column=9)

calc_button_e = CalcButton("e", text="e", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_e.grid(row=2, column=1)
calc_button_pi = CalcButton("\u03C0", text="\u03C0", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_pi.grid(row=2, column=3)
calc_button_sqrt = CalcButton("\u221A", text="\u221A", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_sqrt.grid(row=2, column=5)
calc_button_factorial = CalcButton("!", text="!", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_factorial.grid(row=2, column=7)
calc_button_parentheses_open = CalcButton("(", text="(", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_parentheses_close = CalcButton(")", text=")", width=5, relief=RAISED, fg="White", bg="Black")
calc_button_parentheses_open.grid(row=2, column=9)

calc_button_seven = CalcButton("7", text="7", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_seven.grid(row=3, column=1)
calc_button_eight = CalcButton("8", text="8", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_eight.grid(row=3, column=3)
calc_button_nine = CalcButton("9", text="9", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_nine.grid(row=3, column=5)
calc_button_del = CalcButton("\u2190", text="\u2190", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_del.grid(row=3, column=7)
calc_button_division = CalcButton("\u00F7", text="\u00F7", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_division.grid(row=3, column=9)

calc_button_four = CalcButton("4", text="4", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_four.grid(row=4, column=1)
calc_button_five = CalcButton("5", text="5", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_five.grid(row=4, column=3)
calc_button_six = CalcButton("6", text="6", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_six.grid(row=4, column=5)
calc_button_mod = CalcButton("%", text="%", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_mod.grid(row=4, column=7)
calc_button_multiply = CalcButton("x", text="x", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_multiply.grid(row=4, column=9)

calc_button_one = CalcButton("1", text="1", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_one.grid(row=5, column=1)
calc_button_two = CalcButton("2", text="2", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_two.grid(row=5, column=3)
calc_button_three = CalcButton("3", text="3", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_three.grid(row=5, column=5)
calc_button_power = CalcButton("^", text="^", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_power.grid(row=5, column=7)
calc_button_subtract = CalcButton("-", text="-", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_subtract.grid(row=5, column=9)

calc_button_ac = CalcButton("AC", text="AC", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_ac.grid(row=6, column=1)
calc_button_zero = CalcButton("0", text="0", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_zero.grid(row=6, column=3)
calc_button_radix = CalcButton(".", text=".", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_radix.grid(row=6, column=5)
calc_button_equal = CalcButton("=", text="=", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_equal.grid(row=6, column=7)
calc_button_add = CalcButton("+", text="+", width=5, relief=RAISED, fg="Black", bg="White")
calc_button_add.grid(row=6, column=9)
calc_window.mainloop()
