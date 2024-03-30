
# Sudoku Solver using Constraint Satisfaction Problem (CSP) Algorithm

This Python script provides a solver for Sudoku puzzles utilizing the Constraint Satisfaction Problem (CSP) algorithm. The solver takes an input Sudoku puzzle and returns the solution if it exists. It is implemented using a backtracking search algorithm with constraint propagation.

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
