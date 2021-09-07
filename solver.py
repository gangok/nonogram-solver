import json
import pprint

class NonogramTable:
    FILL = 'O'
    EMPTY = 'X'

    def __init__(self, file):
        self._read_from_file(file)
        self.table = [[None] * self.width for i in range(self.height)]

    def print(self):
        print(self.row_numbers)
        print(self.column_numbers)
        pprint.pprint(self.table)
        pprint.pprint(self.table_solution)
        print(self.is_correct())

    def _read_from_file(self, file):
        dictionary = json.load(file)
        self.height = dictionary['height']
        self.width = dictionary['width']
        self.row_numbers = dictionary['row_numbers']
        self.column_numbers = dictionary['column_numbers']
        self.table_solution = dictionary['table']

    def solve(self):
        has_modified = True
        while has_modified:
            has_modified = False
            for i in range(self.height):
                modified, line = self._solve_line(self.table[i], self.row_numbers[i])
                self.table[i] = line
                if modified:
                    has_modified = True
            for j in range(self.width):
                line = [row[j] for row in self.table]
                modified, line = self._solve_line(line, self.column_numbers[j])
                for i in range(self.height):
                    self.table[i][j] = line[i]
                if modified:
                    has_modified = True

    def _solve_line(self, line, numbers):
        N = len(line)
        unknown_numbers = line.count(None)
        if unknown_numbers == numbers[0]:
            for i in range(N):
                if line[i] == None:
                    line[i] = self.FILL
            return True, line
        else:
            return False, line

    def is_correct(self):
        return self.table == self.table_solution


with open("problem_0.txt", "r") as file:
    table = NonogramTable(file)
    table.solve()
    table.print()

with open("problem_1.txt", "r") as file:
    table = NonogramTable(file)
    table.solve()
    table.print()
