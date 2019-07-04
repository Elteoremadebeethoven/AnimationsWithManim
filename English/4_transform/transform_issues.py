from big_ol_pile_of_manim_imports import *

class TextLike1DArrays(Scene):
	def construct(self):
		text=TextMobject("Te","xt")
		# text=TextMobject("Te","xt")[0] # <- Recent versions
		for i in text:
			self.play(FadeIn(i))
			self.wait()
			self.play(FadeOut(i))
		self.wait()

class TextLike2DArraysV1(Scene):
	def construct(self):
		text=TextMobject("Te","xt")
		# text=TextMobject("Te","xt")[0] # <- Recent versions
		self.play(FadeIn(text[0][0]))
		self.play(FadeIn(text[0][1]))
		self.play(FadeIn(text[1][0]))
		self.play(FadeIn(text[1][1]))
		self.wait()

class TextLike2DArraysV2(Scene):
	def construct(self):
		text=TextMobject("Te","xt")
		for i in text:
			for j in i:
				self.play(FadeIn(j))

		self.wait()

class TextLike2DArraysV3(Scene):
	def construct(self):
		text=TextMobject("Te","xt")
		# text=TextMobject("Te","xt")[0] # <- Recent versions
		for i in range(len(text)):
			for j in range(len(text[i])):
				self.play(FadeIn(text[i][j]))

		self.wait()

class TransformIssues(Scene):
	def construct(self):
		#                   0   1   2
		text_1=TextMobject("A","B","C")
		# text_1=TextMobject("A","B","C")[0] # <- Recent versions
		#                   0
		text_2=TextMobject("B")
		# text_2=TextMobject("B")[0]

		text_2.next_to(text_1,UP,buff=1)

		#Add the elements 0 and 2 of text_1 to screen and text_2
		self.play(
					*[
						FadeIn(text_1[i])
						for i in [0,2]
					],
					FadeIn(text_2)
			)

		self.wait()

		self.play(
					ReplacementTransform(text_2,text_1[1])
			)

		self.wait()
		
class TransformVGroup(Scene):
    def construct(self):
        text_n=TextMobject("A")
        text_v=VGroup(TextMobject("A")).next_to(text_n,DOWN)

        self.play(Write(text_n))

        self.play(ReplacementTransform(text_n,text_v))
	#Solution
	#         ReplacementTransform(text_n,text_v[0])
        self.wait()

class TransformIssuesSolution1(Scene):
	def construct(self):
		#                   0   1   2
		text_1=TextMobject("A","B","C")
		# text_1=TextMobject("A","B","C")[0] # <- Recent versions
		#                   0
		text_2=TextMobject("B")
		# text_2=TextMobject("B")[0]

		text_2.next_to(text_1,UP,buff=1)

		#Add the elements 0 and 2 of text_1 to screen and text_2
		self.play(
					*[
						FadeIn(text_1[i])
						for i in [0,2]
					],
					FadeIn(text_2)
			)

		self.wait()

		self.play(
					# Add [:] to the firts or second parameter
					ReplacementTransform(text_2[:],text_1[1])
			)

		self.wait()

class TransformIssuesSolutionInfallible(Scene):
	def construct(self):
		#                   0   1   2
		text_1=TextMobject("A","B","C")
		# text_1=TextMobject("A","B","C")[0] # <- Recent versions
		#                   0
		text_2=TextMobject("B")
		# text_2=TextMobject("B")[0]

		text_2.next_to(text_1,UP,buff=1)

		#Create a copy of the objects

		text_1_1_c=TextMobject("B")\
				   .match_style(text_1[1])\
				   .match_width(text_1[1])\
				   .move_to(text_1[1])

		#Add the elements 0 and 2 of text_1 to screen and text_2
		self.play(
					*[
						FadeIn(text_1[i])
						for i in [0,2]
					],
					FadeIn(text_2)
			)

		self.wait()

		self.play(
					# Add [:] to the firts or second parameter
					ReplacementTransform(text_2,text_1_1_c)
			)
		self.remove(text_1_1_c)
		self.add(text_1[1])

		self.wait()
