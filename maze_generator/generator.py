from random import choice

from .cell import Cell
from .grid import Grid


class Generator:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.current = self.grid.start
        self.current.visited = True

    def generate(self, verbose: bool = False):
        while not all(cell.visited for cell in self.grid if cell.visitable):
            self.next()
            if verbose:
                print(self.grid)

        for _ in range((self.grid.width + self.grid.height) / 2):
            self.remove_random()
            if verbose:
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
            neighbour = choice(
                [
                    cell
                    for cell in self.current.neighbours
                    if cell.wall_between(self.grid, self.current)
                ]
            )
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

    def remove_random(self) -> Cell:
        self.current = choice([cell for cell in self.grid if cell.visitable])
        while all(
            not cell.wall_between(self.grid, self.current)
            for cell in self.current.neighbours
        ):
            self.current = choice(
                [cell for cell in self.grid if cell.visitable]
            )

        neighbour = choice(
            [
                cell
                for cell in self.current.neighbours
                if cell.wall_between(self.grid, self.current)
            ]
        )
        self.current.remove_wall(self.grid, neighbour)

        return self.current
