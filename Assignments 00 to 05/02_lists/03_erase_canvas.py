#Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.


import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserCanvas:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser Tool")
        
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        
        self.cells = []
        self.create_grid()

        # Create an eraser (invisible, just for tracking movement)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="red")

        # Bind mouse movement to erasing effect
        self.canvas.bind("<B1-Motion>", self.erase)
        self.canvas.bind("<Motion>", self.move_eraser)

    def create_grid(self):
        """Creates a grid of blue cells."""
        self.cells = []
        for x in range(0, CANVAS_WIDTH, CELL_SIZE):
            row = []
            for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
                cell = self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="blue", outline="black")
                row.append(cell)
            self.cells.append(row)

    def erase(self, event):
        """Erases the blue cells under the eraser."""
        x1, y1, x2, y2 = self.canvas.coords(self.eraser)
        for row in self.cells:
            for cell in row:
                cx1, cy1, cx2, cy2 = self.canvas.coords(cell)
                if not (cx2 < x1 or cx1 > x2 or cy2 < y1 or cy1 > y2):  # If overlapping
                    self.canvas.itemconfig(cell, fill="white")

    def move_eraser(self, event):
        """Moves the eraser rectangle to follow the mouse."""
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x - ERASER_SIZE // 2, y - ERASER_SIZE // 2,
                           x + ERASER_SIZE // 2, y + ERASER_SIZE // 2)

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserCanvas(root)
    root.mainloop()
