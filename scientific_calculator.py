from tkinter import *
import math

last_clicked = None
expression = ""


class CalcButton(Button):
	def __init__(self, display_symbol, math_symbol, **kwargs):
		super().__init__(**kwargs)
		self.display_symbol = display_symbol
		self.math_symbol = math_symbol
		self.is_clicked = False


def remove_buttons(*buttons):
	for button in buttons:
		button.grid_remove()


def replace_buttons(*buttons):
	buttons[0].grid(
		row=1,
		column=1
	)
	buttons[1].grid(
		row=1,
		column=3
	)
	buttons[2].grid(
		row=1,
		column=5
	)
	buttons[3].grid(
		row=1,
		column=7
	)
	buttons[4].grid(
		row=2,
		column=9
	)
	if buttons[0] is calc_button_ln:
		buttons[5].config(
			relief=RIDGE,
			bg="Grey",
			fg="White"
		)
	else:
		buttons[5].config(
			relief=RAISED,
			bg="White",
			fg="Black"
		)


def trigger_action(button):
	global last_clicked, expression
	if last_clicked is calc_button_equal or button is calc_button_ac:
		reset_calculator()
	if button is calc_button_del:
		calc_display.delete(len(calc_display.get()) - 1)
	if button is calc_button_equal:
		try:
			result = eval(expression)
		except SyntaxError or NameError or ValueError:
			reset_calculator()
			calc_display.insert(
				calc_display.index(INSERT),
				"Error!"
			)
			return
		calc_display.delete(
			0,
			len(calc_display.get())
		)
		calc_display.insert(
			calc_display.index(INSERT),
			str(result)
		)
	calc_display.insert(
		calc_display.index(INSERT),
		button.display_symbol
	)
	expression += button.math_symbol
	last_clicked = button


def reset_calculator():
	global expression
	calc_display.delete(
		0,
		len(calc_display.get())
	)
	expression = ""


def shift_buttons(shift_button):
	shift_button.is_clicked = not shift_button.is_clicked
	if shift_button.is_clicked:
		remove_buttons(
			calc_button_log,
			calc_button_sin,
			calc_button_cos,
			calc_button_tan,
			calc_button_parentheses_open
		)
		replace_buttons(
			calc_button_ln,
			calc_button_arcsin,
			calc_button_arccos,
			calc_button_arctan,
			calc_button_parentheses_close,
			shift_button
		)
	else:
		remove_buttons(
			calc_button_ln,
			calc_button_arcsin,
			calc_button_arccos,
			calc_button_arctan,
			calc_button_parentheses_close
		)
		replace_buttons(
			calc_button_log,
			calc_button_sin,
			calc_button_cos,
			calc_button_tan,
			calc_button_parentheses_open,
			shift_button
		)


calc_window = Tk()
calc_window.title("Scientific Calculator")
calc_display = Entry(
	width=50,
	borderwidth=10,
	relief=RIDGE,
	fg="White",
	bg="Black"
)
calc_display.grid(
	row=0,
	column=0,
	columnspan=11,
	padx=10,
	pady=10
)
calc_button_log = CalcButton(
	"Log",
	"math.log10",
	text="Log",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_log)
)
calc_button_ln = CalcButton(
	"Ln",
	"math.log",
	text="Ln",
	width=5,
	relief=RAISED,
	fg="White",
	bg="Black",
	command=lambda: trigger_action(calc_button_ln)
)
calc_button_log.grid(
	row=1,
	column=1,
	pady=5
)
calc_button_sin = CalcButton(
	"Sin",
	"math.sin",
	text="Sin",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_sin)
)
calc_button_arcsin = CalcButton(
	"ArcSin",
	"math.asin",
	text="Sin\u207B\u2071",
	width=5,
	relief=RAISED,
	fg="White",
	bg="Black",
	command=lambda: trigger_action(calc_button_arcsin)
)
calc_button_sin.grid(
	row=1,
	column=3,
	pady=5
)
calc_button_cos = CalcButton(
	"Cos",
	"math.cos",
	text="Cos",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_cos)
)
calc_button_arccos = CalcButton(
	"ArcCos",
	"math.acos",
	text="Cos\u207B\u2071",
	width=5,
	relief=RAISED,
	fg="White",
	bg="Black",
	command=lambda: trigger_action(calc_button_arccos)
)
calc_button_cos.grid(
	row=1,
	column=5,
	pady=5
)
calc_button_tan = CalcButton(
	"Tan",
	"math.tan",
	text="Tan",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_tan)
)
calc_button_arctan = CalcButton(
	"ArcTan",
	"math.atan",
	text="Tan\u207B\u2071",
	width=5,
	relief=RAISED,
	fg="White",
	bg="Black",
	command=lambda: trigger_action(calc_button_arctan)
)
calc_button_tan.grid(
	row=1,
	column=7,
	pady=5
)
calc_button_shift = CalcButton(
	"",
	"",
	text="Shift",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: shift_buttons(calc_button_shift)
)
calc_button_shift.grid(
	row=1,
	column=9,
	pady=5
)

calc_button_e = CalcButton(
	"e",
	"math.e",
	text="e",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_e)
)
calc_button_e.grid(
	row=2,
	column=1,
	pady=5
)
calc_button_pi = CalcButton(
	"\u03C0",
	"math.pi",
	text="\u03C0",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_pi)
)
calc_button_pi.grid(
	row=2,
	column=3,
	pady=5
)
calc_button_sqrt = CalcButton(
	"\u221A",
	"math.sqrt(",
	text="\u221A",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_sqrt)
)
calc_button_sqrt.grid(
	row=2,
	column=5,
	pady=5
)
calc_button_factorial = CalcButton(
	"!",
	"math.factorial(",
	text="!",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_factorial)
)
calc_button_factorial.grid(
	row=2,
	column=7,
	pady=5
)
calc_button_parentheses_open = CalcButton(
	"(",
	"(",
	text="(",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_parentheses_open)
)
calc_button_parentheses_close = CalcButton(
	")",
	")",
	text=")",
	width=5,
	relief=RAISED,
	fg="White",
	bg="Black",
	command=lambda: trigger_action(calc_button_parentheses_close)
)
calc_button_parentheses_open.grid(
	row=2,
	column=9,
	pady=5
)
calc_button_seven = CalcButton(
	"7",
	"7",
	text="7",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_seven)
)
calc_button_seven.grid(
	row=3,
	column=1,
	pady=5
)
calc_button_eight = CalcButton(
	"8",
	"8",
	text="8",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_eight)
)
calc_button_eight.grid(
	row=3,
	column=3,
	pady=5
)
calc_button_nine = CalcButton(
	"9",
	"9",
	text="9",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_nine)
)
calc_button_nine.grid(
	row=3,
	column=5,
	pady=5
)
calc_button_del = CalcButton(
	"",
	"",
	text="\u2190",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_del)
)
calc_button_del.grid(
	row=3,
	column=7,
	pady=5
)
calc_button_division = CalcButton(
	"\u00F7",
	"/",
	text="\u00F7",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_division)
)
calc_button_division.grid(
	row=3,
	column=9,
	pady=5
)
calc_button_four = CalcButton(
	"4",
	"4",
	text="4",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_four)
)
calc_button_four.grid(
	row=4,
	column=1,
	pady=5
)
calc_button_five = CalcButton(
	"5",
	"5",
	text="5",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_five)
)
calc_button_five.grid(
	row=4,
	column=3,
	pady=5
)
calc_button_six = CalcButton(
	"6",
	"6",
	text="6",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_six)
)
calc_button_six.grid(
	row=4,
	column=5,
	pady=5
)
calc_button_mod = CalcButton(
	"%",
	"%",
	text="%",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_mod)
)
calc_button_mod.grid(
	row=4,
	column=7,
	pady=5
)
calc_button_multiply = CalcButton(
	"x",
	"*",
	text="x",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_multiply)
)
calc_button_multiply.grid(
	row=4,
	column=9,
	pady=5
)
calc_button_one = CalcButton(
	"1",
	"1",
	text="1",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_one)
)
calc_button_one.grid(
	row=5,
	column=1,
	pady=5
)
calc_button_two = CalcButton(
	"2",
	"2",
	text="2",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_two)
)
calc_button_two.grid(
	row=5,
	column=3,
	pady=5
)
calc_button_three = CalcButton(
	"3",
	"3",
	text="3",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_three)
)
calc_button_three.grid(
	row=5,
	column=5,
	pady=5
)
calc_button_power = CalcButton(
	"^",
	"**",
	text="^",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_power)
)
calc_button_power.grid(
	row=5,
	column=7,
	pady=5
)
calc_button_subtract = CalcButton(
	"-",
	"-",
	text="-",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_subtract)
)
calc_button_subtract.grid(
	row=5,
	column=9,
	pady=5
)
calc_button_ac = CalcButton(
	"",
	"",
	text="AC",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_ac)
)
calc_button_ac.grid(
	row=6,
	column=1,
	pady=5
)
calc_button_zero = CalcButton(
	"0",
	"0",
	text="0",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_zero)
)
calc_button_zero.grid(
	row=6,
	column=3,
	pady=5
)
calc_button_radix = CalcButton(
	".",
	".",
	text=".",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_radix)
)
calc_button_radix.grid(
	row=6,
	column=5,
	pady=5
)
calc_button_equal = CalcButton(
	"",
	"",
	text="=",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_equal)
)
calc_button_equal.grid(
	row=6,
	column=7,
	pady=5
)
calc_button_add = CalcButton(
	"+",
	"+",
	text="+",
	width=5,
	relief=RAISED,
	fg="Black",
	bg="White",
	command=lambda: trigger_action(calc_button_add)
)
calc_button_add.grid(
	row=6,
	column=9,
	pady=5
)
calc_window.mainloop()
