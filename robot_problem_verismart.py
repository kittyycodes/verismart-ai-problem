import sys
class Grid:
    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows

    def is_valid_position(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

class Robot:
    def __init__(self, grid: Grid):
        self.grid = grid
        # starting position 
        self.row = 0
        self.col = 0
        self.direction = 'S'
        # moves
        self.movement_deltas = {
            'N': (-1, 0),
            'S': (1, 0),
            'E': (0, 1),
            'W': (0, -1)
        }

    def change_direction(self, new_direction: str) -> None:
        if new_direction in self.movement_deltas and new_direction != self.direction:
            self.direction = new_direction

    def move(self) -> None:
        delta_row, delta_col = self.movement_deltas[self.direction]
        new_row = self.row + delta_row
        new_col = self.col + delta_col
        # move only if the new position is within grid bounds
        if self.grid.is_valid_position(new_row, new_col):
            self.row = new_row
            self.col = new_col

    def execute_command(self, command: str) -> None:
        for instruction in command:
            if instruction == 'M':
                self.move()
            elif instruction in self.movement_deltas:
                self.change_direction(instruction)
            else:
                raise ValueError(f"Invalid instruction: {instruction}")

    def get_position(self) -> str:
        return f"({self.row},{self.col},{self.direction})"

def main(): #input
    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        command = input("COMMAND: ").strip()

    grid = Grid(5, 4)
    robot = Robot(grid)
    robot.execute_command(command)
    print(f"Robot Location: {robot.get_position()}")

if __name__ == "__main__":
    main()
