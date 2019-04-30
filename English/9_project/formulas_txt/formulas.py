from big_ol_pile_of_manim_imports import *
from tutorial.svg_classes import CheckFormulaByTXT
from io import *

formulas=[]

a_color=RED_B
b_color=BLUE_B
c_color=GREEN_B
x_color=YELLOW_B

for i in range(1,17):
	formula_open=open("tutorial/formulas_txt/formula%de.txt"%i,"r")
	formula=formula_open.readlines()
	formulas.append(TexMobject(*formula).scale(1.7))


for i in range(10):
	formulas[i].set_color_by_tex("a", a_color)
	formulas[i].set_color_by_tex("b", b_color)
	formulas[i].set_color_by_tex("c", c_color)
	formulas[i].set_color_by_tex("x", x_color)

set_color_formulas=[
				(10,
					(
						(a_color,[10,25,31]),
						(b_color,[6,21]),
						(c_color,[26]),
						(x_color,[3]))
					),
				(11,
					(
						(a_color,[6,18,24]),
						(b_color,[3,14]),
						(c_color,[19]),
						(x_color,[0]))
					),
				(12,
					(
						(a_color,[7,18,24]),
						(b_color,[4,14]),
						(c_color,[19]),
						(x_color,[0]))
					),
				(13,
					(
						(a_color,[7,18,23]),
						(b_color,[4,14]),
						(c_color,[20]),
						(x_color,[0]))
					),
				(14,
					(
						(a_color,[13,18]),
						(b_color,[4,9]),
						(c_color,[15]),
						(x_color,[0]))
					),
]
for f,changes in set_color_formulas:
	for colors,symbols in changes:
		for symbol in symbols:
			formulas[f][symbol].set_color(colors)

''' Code:
class ConfigFormula(CheckFormulaByTXT):
	CONFIG={
	"show_elements":[],
	"remove": [],
	"text": formulas[]
	}
'''

class ConfigFormula0(CheckFormulaByTXT):
	CONFIG={
	"show_elements":[],
	"remove": [], #2
	"text": formulas[0]
	}

class ConfigFormula1(CheckFormulaByTXT):
	CONFIG={
	"show_elements":[],
	"remove": [], #2
	"text": formulas[1]
	}