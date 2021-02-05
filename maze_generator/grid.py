from json import dump, load
from typing import Iterator, List, Optional, Tuple

from .cell import Cell


class Grid:
    def __init__(
        self,
        width: int,
        height: int,
        start: Tuple[int, int],
        end: Tuple[int, int],
    ):
        self.width = width
        self.height = height

        self._grid = [
            [
                Cell(
                    x,
                    y,
                    start=((x, y) == start),
                    end=((x, y) == end),
                )
                for y in range(height)
            ]
            for x in range(width)
        ]

        self.start = self[start]
        self.end = self[end]

        for x, column in enumerate(self._grid):
            for y, cell in enumerate(column):
                if x % 2 == 1 or y % 2 == 1:
                    cell.obstacle = True
                else:
                    cell.visitable = True

    def __getitem__(self, pos: Tuple[int, int]) -> Cell:
        x, y = pos
        return self._grid[x][y]

    def __iter__(self) -> Iterator:
        return iter(sum(self._grid, []))

    def __str__(self) -> str:
        return (
            "#" * (self.width + 2)
            + "\n"
            + "\n".join(
                "#" + "".join(str(cell) for cell in line) + "#"
                for line in zip(*self._grid)
            )
            + "\n"
            + "#" * (self.width + 2)
        )

    def reset(self):
        for cell in self:
            cell.reset()

    def to_json(self, filename: Optional[str] = None) -> List[List[int]]:
        json_grid = []

        for colmun in self._grid:
            json_column = []

            for cell in colmun:
                json_column.append(cell.to_json())

            json_grid.append(json_column)

        json_grid = [list(column) for column in zip(*json_grid)]

        if filename is not None:
            with open(filename, "w") as f:
                dump(json_grid, f)

        return json_grid

    @classmethod
    def from_json(cls, filename: str = "grid.json") -> "Grid":
        with open(filename) as f:
            json_grid = load(f)

        self: Grid = cls.__new__(cls)
        self.width = len(json_grid[0])
        self.height = len(json_grid)
        self._grid = []

        for y, json_line in enumerate(json_grid):
            line = []

            for x, json_cell in enumerate(json_line):
                cell = Cell(x, y, obstacle=(json_cell == 1))
                line.append(cell)

                if json_cell == 2:
                    self.start = cell
                    cell.start = True
                    cell.distance_from_start = 0
                elif json_cell == 3:
                    self.end = cell
                    cell.end = True

            self._grid.append(line)

        # invert lines and columns
        self._grid = [list(column) for column in zip(*self._grid)]

        return self
