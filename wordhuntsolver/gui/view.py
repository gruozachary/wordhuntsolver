"""Contains "View" class for GUI"""

import tkinter as tk
import PIL.Image
import PIL.ImageTk

class View:
    """The MVC view for the GUI"""

    root: tk.Tk
    photo_label: tk.Label
    next_button: tk.Button

    def __init__(self, root: tk.Tk):
        self.root = root

        root.geometry("500x500")

        self.photo_label = tk.Label(root)
        self.next_button = tk.Button(root)

        self.photo_label.pack()
        self.next_button.pack()

    def set_image(self, image: PIL.Image.Image):
        """Changes the image displayed on the GUI"""

        resized = image.resize((250, 250))

        photo = PIL.ImageTk.PhotoImage(resized)

        self.photo_label.config(image=photo)
        self.photo_label.image_ref = photo

    # TODO: Type procedure?
    def on_next(self, proc):
        """Given a procedure, will execute when user presses the next button"""

        self.next_button.config(command=proc)
