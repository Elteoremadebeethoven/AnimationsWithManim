from big_ol_pile_of_manim_imports import *
#Import formulas:
from tutorial.formulas_txt.formulas import formulas

class SolveGeneralQuadraticEquation(Scene):
	def construct(self):
		self.import_formulas()
		self.write_formulas()
		self.set_changes()
		self.step_formula(n_step=1,
			changes=self.set_of_changes[0],
			fade=[10],
			path_arc=-PI/2
			)
		self.step_formula(n_step=2,
			changes=self.set_of_changes[1],
			write=[6,14],
			pre_copy=[0],
			pos_copy=[15]
			)
		self.step_formula(n_step=3,
			changes=self.set_of_changes[2],
			pos_write=[10,	11,	13,	14,	15,	16,	18,	20,	28,	29,	31,	32,	33,	34,	36,	38],
			)
		self.step_formula(n_step=4,
			changes=self.set_of_changes[3],
			)
		self.step_formula(n_step=5,
			changes=self.set_of_changes[4],
			fade=[20,27],
			pre_copy=[29],
			pos_copy=[28]
			)
		self.step_formula(n_step=6,
			changes=self.set_of_changes[5],
			fade=[19],
			)
		self.step_formula(n_step=7,
			changes=self.set_of_changes[6],
			pos_write=[25,28],
			)
		self.step_formula(n_step=8,
			changes=self.set_of_changes[7],
			pos_write=[32,26],
			)
		self.step_formula(n_step=9,
			changes=self.set_of_changes[8],
			)
		self.step_formula(n_step=10,
			changes=self.set_of_changes[9],
			pos_write=[0,	1,	16,	18,	20],
			)
		self.step_formula(n_step=11,
			changes=self.set_of_changes[10],
			fade=[0,	1,	2,	12,	14]
			)
		self.step_formula(n_step=12,
			changes=self.set_of_changes[11],
			)
		self.step_formula(n_step=13,
			changes=self.set_of_changes[12],
			fade=[25]
			)
		self.step_formula(n_step=14,
			changes=self.set_of_changes[13],
			)
		#
		c1=SurroundingRectangle(self.formulas[14],buff=0.2)
		c2=SurroundingRectangle(self.formulas[14],buff=0.2)
		c2.rotate(PI)
		self.play(ShowCreationThenDestruction(c1),ShowCreationThenDestruction(c2))
		self.wait(2)

	def import_formulas(self):
		self.formulas=formulas


	def write_formulas(self):
		self.play(Write(self.formulas[0]))

	def set_changes(self):
		self.set_of_changes=[
		#1
		[[
						(	0,	1,	3,	4,	5,	6,	7,	8,	9	),
						(	0,	1,	3,	4,	5,	6,	8,	9,	7	)
		]],
		#2
		[[
						(	0,		1,	3,	4,	5,	6,	7,	8,	9	),
						(	7,		0,	2,	3,	5,	9,	10,	11,	13	)
		]],
		#3
		[[
			(	0,	2,	3,	5,	6,	7,	9,	10,	11,	13,	14,	15	),
			(	0,	2,	3,	5,	6,	7,	9,	21,	22,	24,	25,	26	)
		]],
		#4
		[[
				(	0,	2,	10,	11,	13,	14,	15,	16,	18,	20,	21,	22,	24,	25,	26,	28,	29,	31,	32,	33,	34,	36,	38	,5,6,7,9,3),
				(	1,	11,	2,	0,	4,	5,	6,	7,	9,	11,	12,	13,	15,	16,	17,	19,	20,	22,	23,	24,	25,	27,	29	,4,5,7,1,2)
		]],
		#5
		[[
		(	0,	1,	2,	4,	5,	6,	7,	9,	11,	12,	13,	15,	16,	17,	19,	22,	23,	24,	25,	29),
		(	0,	1,	2,	4,	5,	6,	7,	9,	11,	12,	13,	15,	16,	17,	19,	21,	24,	25,	26,	23)
		]],
		#6
		[[
			(	0,	1,	2,	4,	5,	6,	7,	9,	11,	12,	13,	15,	16,	17,	21,	23,	24,	25,	26,	28	),
			(	0,	1,	2,	4,	5,	6,	7,	9,	11,	12,	23,	25,	26,	27,	14,	16,	17,	18,	19,	21	)
		]],
		#7
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,		21,		23,		25,	26,	27	),
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,		21,		23,		26,	27,	29	)
		]],
		#8
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,		21,		23,		25,	26,	27,	28,	29,	),
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,		21,		23,		25,	27,	28,	29,	30,	)
		]],
		#9
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,		21,		23,		25,	26,	27,	28,	29,	30,		32,	),
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	21,	22,	23,		25,		17,		18,	19,	20,	21,	22,	23,		25,	)
		]],
		#10
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,	20,	21,	22,	23,		25,	),
			(	2,	3,	5,		6,	7,	8,	10,		12,		14,	15,		21,		22,	23,	24,	25,	26,	27,	30,	31,		32,	)
		]],
		#11
		[[
			(				3,		5,	6,	7,	8,		10,					15,	16,		18,		20,	21,	22,	23,	24,	25,	26,	27,			30,	31,	32,	),
			(				0,		1,	3,	4,	5,		6,					8,	9,		10,		12,	14,	15,	16,	17,	18,	19,	20,			21,	24,	25,	)
		]],
		#12
		[[
			(	0,	1,		3,	4,	5,	6,		8,	9,	10,		12,		14,	15,	16,	17,	18,	19,	20,	21,			24,	25,	),
			(	0,	2,		4,	5,	6,	7,		1,	9,	10,		12,		14,	15,	16,	17,	18,	19,	20,	21,			24,	25,	)
		]],
		#13
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,	10,		12,		14,	15,	16,	17,	18,	19,	20,	21,			24,	),
			(	0,	1,	2,		4,	5,	6,	7,		9,	11,		12,		14,	15,	16,	17,	18,	20,	21,	22,			23,	)
		]],
		#14
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,	15,	16,	17,	18,		20,	21,	22,	23,	),
			(	0,	1,	3,		4,	16,	17,	18,		5,		6,	7,		9,	10,	11,	12,	13,		15,	16,	17,	18,	)
		]]
		]

	def step_formula(self,
							pre_write=[],
							pos_write=[],
							pre_fade=[],
							pos_fade=[],
							fade=[],
							write=[],
							changes=[[]],
							path_arc=0,
							n_step=0,
							pre_copy=[],
							pos_copy=[],
							time_pre_changes=0.3,
							time_pos_changes=0.3,
							run_time=2,
							time_end=0.3,
							pre_order=["w","f"],
							pos_order=["w","f"]
							):
		formula_copy=[]
		for c in pre_copy:
			formula_copy.append(self.formulas[n_step-1][c].copy())

		for ani_ in pre_order:
			if len(pre_write)>0 and ani_=="w":
				self.play(*[Write(self.formulas[n_step-1][w])for w in pre_write])
			if len(pre_fade)>0 and ani_=="f":
				self.play(*[FadeOut(self.formulas[n_step-1][w])for w in pre_fade])

		self.wait(time_pre_changes)

		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					self.formulas[n_step-1][i],self.formulas[n_step][j],
					path_arc=path_arc
					)
				for i,j in zip(pre_ind,post_ind)
				],
				*[FadeOut(self.formulas[n_step-1][f])for f in fade if len(fade)>0],
				*[Write(self.formulas[n_step][w])for w in write if len(write)>0],
				*[ReplacementTransform(formula_copy[j],self.formulas[n_step][f])
				for j,f in zip(range(len(pos_copy)),pos_copy) if len(pre_copy)>0
				],
				run_time=run_time
			)

		self.wait(time_pos_changes)

		for ani_ in pos_order:
			if len(pos_write)>0 and ani_=="w":
				self.play(*[Write(self.formulas[n_step][w])for w in pos_write])
			if len(pos_fade)>0 and ani_=="f":
				self.play(*[FadeOut(self.formulas[n_step][w])for w in pos_fade])

		self.wait(time_end)
