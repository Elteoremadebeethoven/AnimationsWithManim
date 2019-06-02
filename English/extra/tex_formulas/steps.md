# Contador de fórmulas en varios frames
Corrobora que la fórmula sea correcta, en este caso es:
```latex
\lim_{x\to\infty}{1\over x}=0
```

Exportala en la terminal usando
```sh
python3 extract_scene.py -g contador_formulas.py Formula
```

```python3
from big_ol_pile_of_manim_imports import *

#exporta -g o -s
def imprimir_formula_paso_1(self,texto,escala,escala_inversa,direccion,excepcion,separacion):
	excepcion=0
	self.add(texto.scale(escala))
	contador = 0
	for j in range(len(texto)):
		elemento = TexMobject("%d" %contador)
		texto[j].set_color(RED)
		self.add(texto[j])
		elemento.set_fill(opacity=1)
		elemento.to_edge(UP)
		self.add(elemento)
		self.wait(0.02)
		elemento.set_fill(opacity=0)
		texto[j].set_color(WHITE)
		contador = contador + 1 

#exporta -s
def imprimir_formula_paso_2(self,texto,escala,escala_inversa,direccion,excepcion,separacion):
	texto.scale(escala).set_color(RED)
	self.add(texto)
	contador = 0
	for j in range(len(texto)):
		permiso_imprimir=True
		for w in excepcion:
			if j==w:
				permiso_imprimir=False
		if permiso_imprimir:
			self.add(texto[j].set_color("#808080"))
		contador = contador + 1

	contador=0
	for j in range(len(texto)):
		permiso_imprimir=True
		elemento = TexMobject("%d" %contador,color=WHITE)
		elemento.scale(escala_inversa)
		elemento.next_to(texto[j],direccion,buff=separacion)
		for w in excepcion:
			if j==w:
				permiso_imprimir=False
		if permiso_imprimir:
			self.add(elemento)
		contador = contador + 1 

class Formula(Scene):
	def construct(self):
		formula=TexMobject("\\lim","_","{","x","\\to","\\infty","}","{","1","\\over","x","}","=","0")
		excepcion=[]
		escala=2.5
		escala_inversa=0.5
		direccion=DOWN
		separacion=0
		imprimir_formula_paso_1(self,formula,escala,escala_inversa,direccion,excepcion,separacion)
```

esto te creará una carpeta con todos los frames de la animación, cada frame corresponderá a un elemento de la fórmula:


<p align="center"><img src ="/Español/extras/formulas_tex/gifs/frames.png" /></p>


# Contador en un sólo frame
## Paso 1:
Corrobora que la fórmula sea correcta usando 
```sh
python extract_scene.py -s contador_formulas.py Formula
```

<p align="center"><img src ="/Español/extras/formulas_tex/gifs/Paso0.png" /></p>

## Paso 2
En la clase "Formula" modifica (NO EN "def imprimir_formula_paso_1" )
```
imprimir_formula_paso_1
```
por
```
imprimir_formula_paso_2
```
y vuelve a compilarlo.

<p align="center"><img src ="/Español/extras/formulas_tex/gifs/Paso1.png" /></p>

## Paso 3
Agrega al arreglo "excepcion" los elementos que están vacios y vuelve a compilar:
```python3
		excepcion=[1,2,6,7,11]
```

<p align="center"><img src ="/Español/extras/formulas_tex/gifs/Paso2.png" /></p>

## Posibles errores
En caso de que sin querer agregues un elemento de más éste aparecerá en rojo indicando que lo incluiste en el arreglo de "excepcion", en este ejemplo eliminaremos la linea de quebrados (elemento 9):
```python3
		excepcion=[1,2,6,7,11,9]
```

<p align="center"><img src ="/Español/extras/formulas_tex/gifs/Paso_error.png" /></p>
