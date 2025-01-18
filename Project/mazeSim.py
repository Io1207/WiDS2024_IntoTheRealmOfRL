from modWilson import *

cols,rows=21,21  #dimensions of the maze

#DO NOT CHANGE THIS PART
#############################################
myMaze=WilsonMazeGenerator(cols,rows)
myMaze.generate_maze()
#############################################
myMaze.get_image()  #optional, feel free to remove

def mazeSolverUsingRL():
    #alter this fuction as you wish to, you can only access the following attributes and functions of class WilsonMazeGenerator:
    # ATTRIBUTES: rows, cols, start=(0,0), grid (contains the array representing the maze. 1 represents free path cells and 0 represents obstacles)
    # FUNCTIONS: get_image (to get a png image of the maze)
    #essentially you can only have information on whether a cell is free path or an obstacle. To check whether the agent has reached 
    #the end of the maze you may only use reached_check function. None of the functions written by you should use prior knowledge of where 
    #the end point of the maze is
    #DO NOT make any changes to WilsonMazeGenerator class
    pathTakenByAgent=[]

    #in the variable pathTakenByAgent you need to give a list of strings like ['L', 'R', 'D'] which represents the 
    #path taken by the agent to the end point. You are supposed to include every single step (even if it is redundant).
    #the method used by you will be judged on the basis of how short of a path it is able to generate as a part of the
    #evaluation we will give the agent mutliple mazes of different dimensions and then find the agent's cumulative score
    myMaze.solution=pathTakenByAgent