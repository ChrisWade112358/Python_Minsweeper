from tkinter import *
import settings

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
    width= 1440,
    height= 180
)

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg= 'blue', # Change color later
    width=360,
    height=540
)

left_frame.place(x=0, y=180)

# Run the window
root.mainloop()


