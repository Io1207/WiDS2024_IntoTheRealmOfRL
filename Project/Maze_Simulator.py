import random
import matplotlib.pyplot as plt

# Do not change the maze generation

class MazeSimulator:
    def _init_(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]  # 1 = wall, 0 = path
        self.start = None
        self.end = None

    def generate_maze(self):
        def is_valid_move(x, y):
            return 0 <= x < self.height and 0 <= y < self.width and self.maze[x][y] == 1

        def dfs(x, y):
            self.maze[x][y] = 0
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid_move(nx, ny):
                    self.maze[x + dx // 2][y + dy // 2] = 0  # Remove the wall
                    dfs(nx, ny)

        start_x, start_y = random.randrange(0, self.height, 2), random.randrange(0, self.width, 2)
        dfs(start_x, start_y)

    def set_start_and_end(self):
        open_cells = [(x, y) for x in range(self.height) for y in range(self.width) if self.maze[x][y] == 0]
        self.start, self.end = random.sample(open_cells, 2)

    def get_maze_array(self):
        maze_array = [[1 if self.maze[x][y] == 0 or (x, y) in [self.start, self.end] else 0 for y in range(self.width)] for x in range(self.height)]
        return maze_array

    def save_maze_image(self, filename="maze.png"):
        maze_copy = [[2 if (x, y) == self.start else 3 if (x, y) == self.end else self.maze[x][y] for y in range(self.width)] for x in range(self.height)]
        plt.figure(figsize=(10, 10))
        plt.imshow(maze_copy, cmap="viridis", origin="upper")
        plt.axis("off")
        plt.savefig(filename)
        plt.close()


def mazeSolverUsingRL():
    #alter this fuction as you wish to, you can access the function in class MazeSimulator or add new functions
    #but DO NOT change the way the maze is being generated
    #you can also add any other functions except the two mentioned here if you wish to but ensure that the final output 
    # is returned from this function only

    #the output of this function should be the path that your agent took in a given course
    #the method used by you will be judged on the basis of how short of a path it is able to generate
    #as a part of the evaluation we will give the agent mutliple mazes of different dimensions and then find the 
    #agent's cumulative score
    pass


# Game flow
if _name_ == "_main_":
    width, height=21,21
    
    simulator = MazeSimulator(width, height)
    simulator.generate_maze()
    simulator.set_start_and_end()
    maze_array = simulator.get_maze_array()
    
    #just for convenience feel free to remove this part in case you don't need it
    print("Maze array:")
    for row in maze_array:
        print(row)
    print(f"Start point: {simulator.start}")
    print(f"End point: {simulator.end}")
    
    simulator.save_maze_image("maze.png")
    print("Maze image saved as 'maze.png'")