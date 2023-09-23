import time
from ortools.sat.python import cp_model

class Impresora(cp_model.CpSolverSolutionCallback):
    """Imprime los pasos intermedios"""

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