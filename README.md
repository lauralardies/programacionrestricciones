# programacionrestricciones

Nuestra dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/programacionrestricciones)
https://github.com/lauralardies/programacionrestricciones

## Problema

El problema de las N-reinas es un problema combinado basado en el juego de ajedrez. Sabiendo
que en el juego del ajedrez las reinas se mueven de adelante a atr ́as y en diagonal, el problema
al que nos enfrentamos nos propone colocar N-reinas en un tablero NxN en donde ninguna reina
est ́e amenazada. Por lo tanto, buscamos que ninguna de las reinas est ́en en la misma fila, columna
o diagonal.

## Archivos

Todos los archivos de esta tarea se encuentran dentro de una carpeta llamada `N-Reinas`. Dentro de ella te puedes encontrar con lo siguiente:

- Un archivo llamado `problema.py` que declara el modelo a usar, define las variables y restricciones, y emplea el solucionador para buscar todas las posibles soluciones.
- Un archivo llamado `impresora.py` que permite mostrar en la terminal las soluciones que se van encontrando.
- Un archivo llamado `main.py` en el que se especifica el tamaño del tablero. Debes introducir un valor N para que se genere un tablero NxN donde buscar las soluciones.
- Un archivo llamado `run.py` mediante el cual se ejecuta el código.
- Un documento LaTeX llamado `Programación_con_Restricciones.pdf` en el se habla de lo que es dicho método de programación y se explica brevemente el código de este repositorio.

## Código

### Código `problema.py`
```
from ortools.sat.python import cp_model
from impresora import Impresora

def juego(tablero):
    # Declaramos modelo.
    modelo = cp_model.CpModel()

    # Definimos variables.
    reinas = [modelo.NewIntVar(0, tablero - 1, f"x_{i}") for i in range(tablero)]

    # Definimos restricciones.
    modelo.AddAllDifferent(reinas)
    modelo.AddAllDifferent(reinas[i] + i for i in range(tablero))
    modelo.AddAllDifferent(reinas[i] - i for i in range(tablero))

    # Llamamos al agente de resolución y calculamos las soluciones.
    solucionador = cp_model.CpSolver()
    impresora = Impresora(reinas)
    solucionador.parameters.enumerate_all_solutions = True
    solucionador.Solve(modelo, impresora)

    # Estadísticas.
    print("Estadísticas")
    print(f"  Conflictos        : {solucionador.NumConflicts()}")
    print(f"  Ramas             : {solucionador.NumBranches()}")
    print(f"  wall time         : {solucionador.WallTime()} s")
    print(f"  Soluciones totales: {impresora.num_soluciones()}")
```

### Código `impresora.py`
```
import time
from ortools.sat.python import cp_model

class Impresora(cp_model.CpSolverSolutionCallback):
    """Imprime las soluciones"""

    def __init__(self, reinas):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__reinas = reinas
        self.__num_soluciones = 0
        self.__hora_comienzo = time.time()

    def num_soluciones(self):
        return self.__num_soluciones

    def on_solution_callback(self):
        hora_ahora = time.time()
        print(
            f"Solución {self.__num_soluciones + 1}, "
            f"tiempo = {hora_ahora - self.__hora_comienzo} s"
        )
        self.__num_soluciones += 1

        todo_reinas = range(len(self.__reinas))
        for i in todo_reinas:
            for j in todo_reinas:
                if self.Value(self.__reinas[j]) == i:
                    print("R", end=" ")
                else:
                    print("_", end=" ")
            print()
        print()
```

### Código `main.py`
```
import sys
from problema import juego

def main():
    print('Selecciona el tamaño de tu tablero:')
    tablero = int(input('>>'))
    if len(sys.argv) > 1:
        tablero = int(sys.argv[1])
    juego(tablero)
```

### Código `run.py`
```
from main import main

if __name__ == "__main__":
    main()
```

## Links
Hemos hecho el ejemplo de [OR-Tools](https://developers.google.com/optimization/cp/queens?hl=es-419)
https://developers.google.com/optimization/cp/queens?hl=es-419
