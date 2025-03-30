import random
import numpy as np

def generate_equation(num_variables):
    coefficients = [random.randint(-10, 10) for _ in range(num_variables)]
    constant = random.randint(-20, 20)
    return coefficients, constant

def solve_system(equations):
    matrix = np.array([eq[0] for eq in equations])
    constants = np.array([eq[1] for eq in equations])

    try:
        solution = np.linalg.solve(matrix, constants)
        return "Solution unique", solution
    except np.linalg.LinAlgError:
        rank_matrix = np.linalg.matrix_rank(matrix)
        rank_augmented = np.linalg.matrix_rank(np.column_stack((matrix, constants)))

        if rank_matrix < rank_augmented:
            return "Incompatible", None
        else:
            return "Indéterminé", None

def generate_system(num_equations, num_variables):
    return [generate_equation(num_variables) for _ in range(num_equations)]

def analyze_system(system):
    result, solution = solve_system(system)
    print(f"Le système est : {result}")
    if solution is not None:
        print(f"Solution : {solution}")
