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

    def __str__(self) -> str:
        if self.obstacle:
            return "#"
        elif self.start:
            return "O"
        elif self.end:
            return "X"
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
