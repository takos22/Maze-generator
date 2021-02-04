from maze_generator import Generator, Grid

grid = Grid(21, 21, (0, 0), (20, 20))
gen = Generator(grid)
gen.generate()
grid.to_json("grid.json")
