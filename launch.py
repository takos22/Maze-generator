from maze_generator import Grid, Window

grid = Grid(21, 21, (0, 0), (20, 20))
Window(grid).run()
grid.to_json("grid.json")
