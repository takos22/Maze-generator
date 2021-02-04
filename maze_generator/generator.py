from random import choice
import time

from .cell import Cell
from .grid import Grid


class Generator:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.current = self.grid.start
        self.current.visited = True

    def generate(self):
        while not all(cell.visited for cell in self.grid if cell.visitable):
            self.next()
            print(self.grid)

    def next(self) -> Cell:
        self.current.add_neighbours(self.grid)
        open_neighbours = [
            neighbour
            for neighbour in self.current.neighbours
            if not neighbour.visited
        ]

        if open_neighbours:
            next = choice(
                [
                    neighbour
                    for neighbour in self.current.neighbours
                    if not neighbour.visited
                ]
            )
            self.current.remove_wall(self.grid, next)

        else:
            neighbour = choice(list(self.current.neighbours))
            self.current.remove_wall(self.grid, neighbour)
            next = choice(
                [
                    cell
                    for cell in self.grid
                    if cell.visitable and not cell.visited
                ]
            )

        self.current = next
        self.current.visited = True

        return self.current
