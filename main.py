from tkinter import *
import settings
import utilities

root = Tk()
# Override the settings of the window
root.configure(
    bg='#f39a03'
)
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(FALSE, FALSE)
root.title("Python_Minesweeper")

top_frame = Frame(
    root,
    bg= 'red', #Change later
    width= utilities.width_prct(100),
    height= utilities.height_prct(25)
)

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg= 'blue', # Change color later
    width=utilities.width_prct(25),
    height=utilities.height_prct(75)
)

left_frame.place(x=0, y=180)

# Run the window
root.mainloop()


