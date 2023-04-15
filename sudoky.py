import random

class Sudoku:
    def __init__(self):
        self._matr = [[0 for _ in range(9)] for _ in range(9)]


    def _n_in_row(self, n, i):
        return n in self._matr[i]


    def _n_in_col(self, n, j):
        return n in [row[j] for row in self._matr]


    def _n_in_quad(self, n, i, j):
        i = (i // 3) * 3
        j = (j // 3) * 3
        for k in range(i, i + 3):
            for l in range(j, j + 3):
                if self._matr[k][l] == n:
                    return True
        return False


    def _candidates(self, i, j):
        candidates = []
        for n in range(1, 10):
            if self._n_in_row(n, i):
                continue
            if self._n_in_col(n, j):
                continue
            if self._n_in_quad(n, i, j):
                continue

            candidates.append(n)

        return candidates


    def _solve(self, i, j):
        for k in range(i, 9):
            for l in range(j, 9):
                # cell not empty, just ignore it
                if self._matr[k][l] != 0:
                    continue
                
                candidates = self._candidates(k, l)
                for n in candidates:
                    self._matr[k][l] = n
                    if self._solve(k, l + 1):
                        return True

                # No more candidates to test. Solve failed. Reset square value and go back.
                self._matr[k][l] = 0
                return False

            j = 0 # next row start from the beginning

        # Solved :D
        return True


    def solve(self):
        return self._solve(0, 0)


    # TODO: Fancy formatting for displaying sudoku matrix
    def print(self) -> None:
        for i in range(0, 9):
            for j in range(0, 9):
                print(self._matr[i][j], end=" ")
            print()
        print("---------------------")

if __name__ == "__main__":
    sudoku = Sudoku()
