class Sudoku:
    def __init__(self) -> None:
        self.table = [0 for _ in range(81)]
    
    def __in_row(self, number, i) -> bool:
        row_start = i // 9 * 9
        return number in self.table[row_start:row_start+9]

    def __in_column(self, number, i) -> bool:
        col_start = i % 9
        return number in self.table[col_start:81:9]
    
    def __in_quad(self, number, i) -> bool:
        row = i // 9 // 3 * 3
        col = i % 9 // 3 * 3

        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if number == self.table[9 * r + c]:
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
        for i in range(start, 81):
            if self.table[i] != 0:
                continue

            candidates = self.__candidates(i)

            for candidate in candidates:
                self.table[i] = candidate

                if self.__solve(start=i + 1):
                    return True
            
            self.table[i] = 0
            return False

        return True

    def solve(self) -> None:
        if not self.__solve(start=0):
            raise ValueError("Sudoku is impossible")

    # TODO: Fancy formatting for displaying sudoku table
    def print(self) -> None:
        for r in range(0, 9):
            for c in range(0, 9):
                print(self.table[9 * r + c], end=" ")
            print()
        print("---------------------")

    # TODO: implement function to load sudoku input from file
    def load_file(self, rpath) -> bool:
        return True

if __name__ == "__main__":
    sudoku = Sudoku()

    sudoku.solve()

    sudoku.print()

