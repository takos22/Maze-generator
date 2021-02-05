from maze_generator import Grid, Window, Generator

grid = Grid(21, 21, (0, 0), (20, 20))
Window(grid).run()
# Generator(grid).generate(True)
grid.to_json("grid.json")
