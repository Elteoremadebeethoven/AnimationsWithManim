# Bad animation with Transform

```python3
class TransformIssues(Scene):
	def construct(self):
		#                   0   1   2
		text_1=TextMobject("A","B","C")
		#                   0
		text_2=TextMobject("B")

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
```

<p align="center"><img src ="/English/4_transform/gifs/TransformIssues.gif" /></p>

```python3
class TransformIssuesSolution1(Scene):
	def construct(self):
		#                   0   1   2
		text_1=TextMobject("A","B","C")
		#                   0
		text_2=TextMobject("B")

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
```

<p align="center"><img src ="/English/4_transform/gifs/TransformIssuesSolution1.gif" /></p>

```python3
class TransformIssuesSolutionInfallible(Scene):
	def construct(self):
		#                   0   1   2
		text_1=TextMobject("A","B","C")
		#                   0
		text_2=TextMobject("B")

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
```


<p align="center"><img src ="/English/4_transform/gifs/TransformIssuesSolutionInfallible.gif" /></p>

# For more information see [this](https://github.com/3b1b/manim/issues/425).
