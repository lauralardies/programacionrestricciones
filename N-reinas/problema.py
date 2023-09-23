from ortools.sat.python import cp_model
from impresora import Impresora

def juego(tablero):
    modelo = cp_model.CpModel()

    reinas = [modelo.NewIntVar(0, tablero - 1, f"x_{i}") for i in range(tablero)]

    modelo.AddAllDifferent(reinas)

    modelo.AddAllDifferent(reinas[i] + i for i in range(tablero))
    modelo.AddAllDifferent(reinas[i] - i for i in range(tablero))

    soludionador = cp_model.CpSolver()
    impresora = Impresora(reinas)
    soludionador.parameters.enumerate_all_solutions = True
    soludionador.Solve(modelo, impresora)