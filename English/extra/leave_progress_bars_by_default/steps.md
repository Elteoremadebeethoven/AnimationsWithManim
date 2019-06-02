# Cómo programar barras de progreso por defecto.
## 1. Abre ```manimlib/config.py``` y realizar los siguientes cambios:

### 1.1 Realiza los cambios en la linea 101, 102 y 103 como se muestra en la imagen.

En la linea 101 cambia ```"--leave_progress_bars"``` por ```"--remove_progress_bars"```.

En la linea 102 cambia ```"store_true"``` por ```"store_false"```.

Opcional: En la linea 103 cambia ```"Leave progress bars displayed in terminal"``` por ```"Remove progress bars displayed in terminal"```.

```python3
        parser.add_argument(
            "--remove_progress_bars",
            action="store_false",
            help="Remove progress bars displayed in terminal",
        )
```
<p align="center"><img src ="/Español/extras/programar_barras_progreso_por_defecto/capturas/capt1.png" /></p>

### 1.2 Realiza el cambio que se ve en la linea 183.

Cambia ```python3 "leave_progress_bars": args.leave_progress_bars``` por ```python3 "remove_progress_bars": args.remove_progress_bars```.

```python3
        "remove_progress_bars": args.remove_progress_bars
```
<p align="center"><img src ="/Español/extras/programar_barras_progreso_por_defecto/capturas/capt2.png" /></p>

## 2. Abre ```manimlib/extract_scene.py``` y realiza el siguiente cambio en la linea 146.

Cambia ```python3 "leave_progress_bars",``` por ```python3 "remove_progress_bars",```.

```python3
        "remove_progress_bars",
```
<p align="center"><img src ="/Español/extras/programar_barras_progreso_por_defecto/capturas/capt3.png" /></p>

## 3. Abre ```manimlib/scene/scene.py``` y realiza los siguientes cambios.

### 3.1 En la linea 31 cambia ```python3 "leave_progress_bars": False``` por ```python3 "remove_progress_bars": False```.

```python3
        "remove_progress_bars": False,
```
<p align="center"><img src ="/Español/extras/programar_barras_progreso_por_defecto/capturas/capt4.png" /></p>


### 3.2 En la linea 31 cambia ```python3 leave=self.leave_progress_bars,``` por ```python3 leave=self.remove_progress_bars,```.

```python3
            leave=self.remove_progress_bars,
```
<p align="center"><img src ="/Español/extras/programar_barras_progreso_por_defecto/capturas/capt5.png" /></p>