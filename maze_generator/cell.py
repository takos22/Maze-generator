from typing import Set


class Cell:
    def __init__(
        self,
        x: int,
        y: int,
        start: bool = False,
        end: bool = False,
        obstacle: bool = False,
    ):
        self.x = x
        self.y = y
        self.pos = (x, y)

        self.start = start
        self.end = end
        self.obstacle = obstacle

        self.neighbours: Set["Cell"] = set()
        self.visited = False
        self.visitable = False

    def __str__(self) -> str:
        if self.obstacle:
            return "#"
        elif self.start:
            return "O"
        elif self.end:
            return "X"
        elif self.visited:
            return "."
        return " "

    def __repr__(self) -> str:
        return str(self.pos)

    def to_json(self) -> int:
        if self.obstacle:
            return 1
        elif self.start:
            return 2
        elif self.end:
            return 3
        return 0

    def add_neighbours(self, grid) -> set:
        if self.x > 1 and not grid[self.x - 2, self.y].obstacle:
            self.neighbours.add(grid[self.x - 2, self.y])  # left

        if self.x + 2 < grid.width and not grid[self.x + 2, self.y].obstacle:
            self.neighbours.add(grid[self.x + 2, self.y])  # right

        if self.y > 1 and not grid[self.x, self.y - 2].obstacle:
            self.neighbours.add(grid[self.x, self.y - 2])  # top

        if self.y + 2 < grid.height and not grid[self.x, self.y + 2].obstacle:
            self.neighbours.add(grid[self.x, self.y + 2])  # bottom

        return self.neighbours

    def remove_wall(self, grid, next: "Cell") -> "Cell":
        cell = None

        if self.x < next.x:
            cell = grid[self.x + 1, self.y]
        elif self.x > next.x:
            cell = grid[self.x - 1, self.y]
        elif self.y < next.y:
            cell = grid[self.x, self.y + 1]
        elif self.y > next.y:
            cell = grid[self.x, self.y - 1]

        cell.obstacle = False
        cell.visited = True
        return cell
