import random
import matplotlib.pyplot as plt

class WilsonMazeGenerator:
    def __init__(self,height,width):
        """
        Initialising the class object
        """   
        self.cols = 2*(width//2) + 1  
        self.rows = 2*(height//2) + 1 
        
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.visited = []    
        self.unvisited = []  
        self.path = dict()  
        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]
        self.generated = False
        self.solution = []

        self.start = (0,0)
        self.end = (self.rows-1,self.cols-1)  ##change this

    def generate_end(self):
        """
        choosing random end point
        """
        zero_indices = [(i, j) for i, row in enumerate(self.grid) for j, val in enumerate(row) if val == 1]
        tent_end=random.choice(zero_indices)
        while tent_end==(0,0):
            tent_end=random.choice(zero_indices)
        self.end=tent_end
        pass

    def generate_maze(self):
        """
        generating maze using the wilson algorithm
        """
        self.initialize_grid()

        current = self.unvisited.pop(random.randint(0,len(self.unvisited)-1))
        self.visited.append(current)
        self.cut(current)
 
        while len(self.unvisited) > 0:
            first = self.unvisited[random.randint(0,len(self.unvisited)-1)]
            current = first
            while True:
                dirNum = random.randint(0,3)
                while not self.is_valid_direction(current,dirNum):
                    dirNum = random.randint(0,3)
                self.path[current] = dirNum
                current = self.get_next_cell(current,dirNum,2)
                if (current in self.visited): 
                    break

            current = first 
            while True:
                self.visited.append(current)
                self.unvisited.remove(current) 
                self.cut(current)

                dirNum = self.path[current]
                crossed = self.get_next_cell(current,dirNum,1)
                self.cut(crossed) 

                current = self.get_next_cell(current,dirNum,2)
                if (current in self.visited): 
                    self.path = dict() 
                    break
                
        self.generated = True
        self.generate_end()

    def get_image(self,filename="maze.png"):
        """
        Saving an image of the maze, only to help with visualization
        """
        maze_copy = [[2 if (x, y) == self.start else 3 if (x, y) == self.end else self.grid[x][y] for y in range(self.cols)] for x in range(self.rows)]
        plt.figure(figsize=(10, 10))
        plt.imshow(maze_copy, cmap="viridis", origin="upper")
        plt.savefig(filename)
        plt.close()

    #Part of maze generation DO NOT MODIFY            
    def get_next_cell(self,cell,dirNum,fact):
        dirTup = self.directions[dirNum]
        return (cell[0]+fact*dirTup[0],cell[1]+fact*dirTup[1])

    #Part of maze generation DO NOT MODIFY
    def is_valid_direction(self,cell,dirNum):
        newCell = self.get_next_cell(cell,dirNum,2)
        tooSmall = newCell[0] < 0 or newCell[1] < 0
        tooBig = newCell[0] >= self.rows or newCell[1] >= self.cols
        return not (tooSmall or tooBig)

    #Part of maze generation DO NOT MODIFY
    def initialize_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = 0
                
        # fill up unvisited cells
        for r in range(self.rows):
            for c in range(self.cols):
                if r % 2 == 0 and c % 2 == 0:
                    self.unvisited.append((r,c))

        self.visited = []
        self.path = dict()
        self.generated = False

    #Part of maze generation, DO NOT MODIFY
    def cut(self,cell):
        self.grid[cell[0]][cell[1]] = 1


def reached_check(maze: WilsonMazeGenerator, agentPos):
    """
    checking whether the agent has reached the goal of the maze
    """
    return agentPos==(maze.end[0],maze.end[1])