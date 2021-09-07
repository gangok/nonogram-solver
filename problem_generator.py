import json
import pprint
import random

class NonogramTable:
    FILL = 'O'
    EMPTY = 'X'

    def __init__(self):
        self.height = 10
        self.width = 10
        self.table = [[None] * self.width for i in range(self.height)]
        self.row_numbers = [None] * self.height
        self.column_numbers = [None] * self.width

    def print(self):
        print(self.row_numbers)
        print(self.column_numbers)
        pprint.pprint(self.table)

    def write_to_file(self, file):
        dictionary = {'height': table.height, 'width': table.width, 'row_numbers': table.row_numbers, 'column_numbers': table.column_numbers, 'table': table.table}
        json.dump(dictionary, file)

    def generate_random_table(self):
        for i in range(self.height):
            for j in range(self.width):
                self.table[i][j] = random.choice([self.FILL, self.EMPTY])
    def generate_numbers(self):
        # Generate row numbers
        for i in range(self.height):
            is_pre_cell_fill = False
            self.row_numbers[i] = []
            for j in range(self.width):
                if self.table[i][j] == self.FILL:
                    if is_pre_cell_fill:
                        self.row_numbers[i][-1] += 1
                    else:
                        self.row_numbers[i].append(1)
                    is_pre_cell_fill = True
                else:
                    is_pre_cell_fill = False
        # Generate column numbers
        for j in range(self.width):
            is_pre_cell_fill = False
            self.column_numbers[j] = []
            for i in range(self.height):
                if self.table[i][j] == self.FILL:
                    if is_pre_cell_fill:
                        self.column_numbers[j][-1] += 1
                    else:
                        self.column_numbers[j].append(1)
                    is_pre_cell_fill = True
                else:
                    is_pre_cell_fill = False


table = NonogramTable()
table.generate_random_table()
table.generate_numbers()
table.print()

with open("problem_temp.txt", "w") as file:
    table.write_to_file(file)