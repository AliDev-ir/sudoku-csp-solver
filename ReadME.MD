
# Sudoku Solver using Constraint Satisfaction Problem (CSP) Algorithm

This Python script provides a solver for Sudoku puzzles utilizing the Constraint Satisfaction Problem (CSP) algorithm. The solver takes an input Sudoku puzzle and returns the solution if it exists. It is implemented using a backtracking search algorithm with constraint propagation.

## Constraint Satisfaction Problem (CSP)

A Constraint Satisfaction Problem (CSP) is a mathematical problem where a set of variables must be assigned values subject to specified constraints. These problems are widespread and can be found in various domains, including artificial intelligence, operations research, and computer science.

### Components of a CSP

1. **Variables**: These are the entities that need to be assigned values. In the context of a Sudoku puzzle, each cell represents a variable that must be assigned a digit.

2. **Domains**: Each variable has a domain, which is the set of possible values it can take. In Sudoku, the domain of each cell is the set of digits from 1 to 9.

3. **Constraints**: Constraints define the relationships between variables. They specify which combinations of variable assignments are valid. In Sudoku, constraints dictate that each row, column, and block must contain unique digits.

### Solving CSPs

Solving a CSP involves finding a valid assignment of values to variables that satisfies all constraints. Various algorithms can be used to solve CSPs, including backtracking search, constraint propagation, and local search techniques.

- **Backtracking Search**: This is a systematic algorithm that explores possible assignments for variables, backtracking when it encounters constraints that cannot be satisfied. It tries different values for each variable until a solution is found or no valid assignments remain.

- **Constraint Propagation**: This technique involves iteratively applying constraints to reduce the domain of variables. By eliminating inconsistent values, constraint propagation narrows down the search space, making it easier to find solutions.

- **Local Search**: Unlike systematic search algorithms like backtracking, local search methods iteratively improve upon partial solutions by making small changes. Techniques like simulated annealing and genetic algorithms can be used to explore the solution space efficiently.

### Applications of CSP

CSPs have applications in various fields, including:

- **Puzzle Solving**: Problems like Sudoku, crosswords, and logic puzzles can be formulated as CSPs and solved using constraint satisfaction techniques.

- **Planning and Scheduling**: CSPs can be used to model scheduling problems, such as employee shifts, project timelines, and resource allocation.

- **Routing and Optimization**: In transportation and logistics, CSPs can help optimize routes, vehicle assignments, and delivery schedules while considering constraints like time windows and capacity limits.

By understanding and applying CSP techniques, you can effectively solve problems that involve assigning values to variables subject to constraints, making it a valuable tool in problem-solving across diverse domains.

## How to Use

### Prerequisites
- Python 3.x

### Running the Solver
1. Clone the repository to your local machine:

```bash
git clone https://github.com/AliDev-ir/sudoku-csp-solver.git
```

2. Navigate to the project directory:

```bash
cd sudoku-csp-solver
```

3. Run the script:

```bash
python sudoku_solver.py
```

4. Enter the Sudoku puzzle row by row, with empty cells represented by `0`.

### Input Format
Provide the Sudoku puzzle row by row, with each row containing 9 digits. Use `0` to represent empty cells.

Example Input:
```
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```

### Output Format
The solver will output the solved Sudoku puzzle in the console.

Example Output:
```
534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179
```

## Algorithm Overview
- The script implements a backtracking search algorithm with constraint propagation to solve Sudoku puzzles.
- It initializes variables representing the Sudoku grid, constraints, and potential solutions.
- The solver iterates through each cell in the puzzle, attempting to assign a valid digit based on constraints.
- If a cell cannot be assigned a digit without violating constraints, the algorithm backtracks to the previous state and tries a different digit.
- The process continues until a solution is found or all possibilities have been exhausted.

## Acknowledgements
This Sudoku solver script was developed by [Your Name]. Feel free to contribute to the project by submitting bug fixes or enhancements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or suggestions, please feel free to contact [Ali vaez](mailto:AliVaez4882@gmail.com). Contributions are welcome!
