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

Para correr el algoritmo deseado sobre el sokoban modificar la [configuración](configs/config.json), especificando el método de búsqueda deseado (BFS, DFS, Greedy_\<heuristic>, A_star_\<heuristic>), el board (board1, board2, ..., board9)
Para el caso de greedy y a_star **hay** que reemplazar \<heuristic> por una de las siguientes opciones (euc/man/no_corners/no_dead)
```sh
pipenv run python main.py
```
Se guardará el resultado en la carpeta [`results`](/results/)

Para abrir el JupyterLab donde se realizaron las pruebas simplemente correr el comando

```sh
pipenv run jupyter lab
```
Finalmente, abrir el archivo `analysis.ipynb`
