class Sudoku:
    def __init__(self) -> None:
        self.__matrix = [0 for _ in range(81)]
    
    def __in_row(self, number, i) -> bool:
        row_start = i // 9 * 9
        return number in self.__matrix[row_start:row_start+9]

    def __in_column(self, number, i) -> bool:
        col_start = i % 9
        return number in self.__matrix[col_start:81:9]
    
    def __in_quad(self, number, i) -> bool:
        row = i // 9 // 3 * 3
        col = i % 9 // 3 * 3

        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if number == self.__matrix[9 * r + c]:
                    return True
        
        return False

    def __candidates(self, i) -> list:
        numbers = [n for n in range(1, 10)]
        candidates = []

        for number in numbers:
            if self.__in_row(number, i):
                continue
            if self.__in_column(number, i):
                continue
            if self.__in_quad(number, i):
                continue

            candidates.append(number)

        return candidates

    def __solve(self, start) -> bool:
        # go through all squares
        for i in range(start, 81):
            # we don't care about filled squares. Just skip.
            if self.__matrix[i] != 0:
                continue
            
            candidates = self.__candidates(i)

            # for each candidate, place it in the square and go forward with the solve
            for candidate in candidates:
                self.__matrix[i] = candidate

                # Further solves were correct. Then, this one is correct. Return True
                if self.__solve(start=i + 1):
                    return True
            
            # No more candidates to test. Solve failed. Reset square value and go back
            self.__matrix[i] = 0
            return False

        # Solved :D
        return True

    def solve(self) -> None:
        if not self.__solve(start=0):
            raise ValueError("Sudoku is impossible")

    # TODO: Fancy formatting for displaying sudoku matrix
    def print(self) -> None:
        for r in range(0, 9):
            for c in range(0, 9):
                print(self.__matrix[9 * r + c], end=" ")
            print()
        print("---------------------")

    def load_file(self, rpath) -> bool:
        import os
        path = os.path.join(os.getcwd(), rpath)

        if not os.path.exists(path):
            return False

        file = open(path, "r")
        i = 0

        for value in file.read().split():
            if value != "\n":
                self.__matrix[i] = int(value)
                i += 1

        return True

if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.load_file("assets/s01a.txt")
    sudoku.print()

    sudoku.solve()

    sudoku.print()
