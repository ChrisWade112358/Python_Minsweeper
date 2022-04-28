from tkinter import Button
import tkinter.font as font
import random
import settings
class Cell:
    all = []
    def __init__(self,x, y,):
        self.is_mine = False,
        self.cell_btn_object = None
        self.x = x
        self.y = y
        #append the object to the Cell.all list
        Cell.all.append(self)
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            bg=settings.bg['red'], # bg cannot be changed on a Mac OS due to OS overriding tkinter (I know this sucks)
                                   # Mac will only display buttons with a white background
            fg=settings.bg['red'],
            font= font.Font(weight="bold")



        )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-2>', self.right_click_actions) # Right Click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine == True:
            print("Is Potato")
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine == True:
                counter += 1
        return counter

    def show_cell(self):
        self.cell_btn_object.configure(text=f"{self.surrounded_cells_mines_length}", fg= settings.bg["blue"])




    def show_mine(self):
        # A logic to interrupt the game and display a message that player lost
        self.cell_btn_object.configure(text='Boom!')

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

    @staticmethod
    def randomize_mines():
        picked_cells= random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        print(picked_cells)
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"