from json import dump
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
