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