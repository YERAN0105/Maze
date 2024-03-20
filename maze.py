import random
import tkinter as tk
from queue import PriorityQueue


class Maze:
    def __init__(self, width, height): #instance of the class
        self.width = width
        self.height = height
        self.start_node = None           #used to represent the grid
        self.goal_node = None
        self.barrier_nodes = set()
        self.time_taken = 0

    def generate_maze(self):
        # Create maze grid
        maze_grid = [[' ' for _ in range(self.width)] for _ in range(self.height)] #creating the maze grid with blanks row by row

        # Set up start node randomly in the first two columns
        self.start_node = (random.randint(0, 1), random.randint(0, self.height - 1))

        # Set up goal node randomly in the last two columns
        self.goal_node = (random.randint(self.width - 2, self.width - 1), random.randint(0, self.height - 1))

        # Set up barrier nodes
        while len(self.barrier_nodes) < 4:
            barrier_node = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if barrier_node != self.start_node and barrier_node != self.goal_node: #checking if the barrier node is equal to start node or goal node
                self.barrier_nodes.add(barrier_node)

        # Print the maze details
        print("Maze Setup:")
        print(f"Start Node: {self.start_node}")
        print(f"Goal Node: {self.goal_node}")
        print(f"Barrier Nodes: {self.barrier_nodes}")

        # Update maze grid with start, goal, and barrier nodes
        maze_grid[self.start_node[1]][self.start_node[0]] = 'S'
        maze_grid[self.goal_node[1]][self.goal_node[0]] = 'G'
        for barrier_node in self.barrier_nodes:
            maze_grid[barrier_node[1]][barrier_node[0]] = 'B'

        return maze_grid

class MazeGUI:
    def __init__(self, master, maze):
        self.master = master
        self.maze = maze
        self.canvas_size = 400
        self.canvas = tk.Canvas(master, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack()
        # Add buttons
        self.button_a_star = tk.Button(master, text="A*", command=self.run_a_star)
        self.button_a_star.pack(side=tk.LEFT, padx=10)

        self.button_dfs = tk.Button(master, text="DFS", command=self.run_dfs)
        self.button_dfs.pack(side=tk.LEFT, padx=10)

        self.button_reset = tk.Button(master, text="Reset", command=self.reset)
        self.button_reset.pack(side=tk.RIGHT, padx=10)
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                if self.maze[y][x] == 'S':
                    self.start_node = (x, y)
                elif self.maze[y][x] == 'G':
                    self.goal_node = (x, y)
        self.height = 6
        self.width = 6
        self.draw_maze()

    def draw_maze(self):
        cell_size = self.canvas_size // len(self.maze[0])
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                cell_type = self.maze[y][x]
                color = 'white' if cell_type == ' ' else 'black' if cell_type == 'B' else 'green' if cell_type == 'S' else 'red'
                self.canvas.create_rectangle(x * cell_size, y * cell_size,
                                             (x + 1) * cell_size, (y + 1) * cell_size,
                                             fill=color, outline='black')

    def reset(self):
        cell_size = self.canvas_size // len(self.maze[0])
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                cell_type = self.maze[y][x]
                color = 'white' if cell_type == ' ' else 'black' if cell_type == 'B' else 'green' if cell_type == 'S' else 'red'
                self.canvas.create_rectangle(x * cell_size, y * cell_size,
                                             (x + 1) * cell_size, (y + 1) * cell_size,
                                             fill=color, outline='black')
    def run_a_star(self):

        print("Running A* algorithm")

    def run_dfs(self):

        print("Running DFS algorithm")

if __name__ == "__main__":
    maze_instance = Maze(6, 6)
    maze_grid = maze_instance.generate_maze()

    root = tk.Tk()
    root.title("Maze Visualization")

    maze_gui = MazeGUI(root, maze_grid)

    root.mainloop()