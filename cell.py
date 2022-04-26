from tkinter import Button
import settings
class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine,
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            bg=settings.bg['gree'],
            text='Text'
        )
        self.cell_btn_object = btn