# TP1 SIA - Métodos de Búsqueda

## Introducción

Trabajo práctico para la materia de Sistemas de Inteligencia Artificial en el ITBA.
Se buscó implementar los métodos de búsqueda: BFS, DFS, Global Greedy Search y A*; y aplicar estos en el juego de Sokoban, que también hubo que implementar.

[Enunciado](docs/Enunciado%20TP1.pdf)

### Requisitos:

- Python3 (La aplicación se probó en la versión de Python 3.11.*)
- pip3
- [pipenv](https://pypi.org/project/pipenv)

### Instalación 

En caso de no tener python, descargarlo desde la [página oficial](https://www.python.org/downloads/release/python-3119/)

Utilizando pip (o pip3 en mac/linux) instalar la dependencia de **pipenv**

```sh
pip install pipenv
```

Parado en la carpeta del proyecto ejecutar

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual

## Ejecución

Para correr el algoritmo deseado sobre el sokoban modificar la [configuración](configs/config.json), especificando el método de búsqueda deseado (BFS, DFS, Greedy, A*), el board (board1, board2, board3, board4); y finalmente correr:
```sh
pipenv run python src/main.py
```
Se guardará el resultado en `result.txt`

Para observar los gráficos sacados en _Jupyter Notebook_ correr:

```sh
pipenv run jupyter notebook
```
Finalmente, abrir el archivo `main.ipynb`
