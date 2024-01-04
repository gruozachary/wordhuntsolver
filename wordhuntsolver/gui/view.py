"""Contains "View" class for GUI"""

import tkinter as tk
import PIL.Image
import PIL.ImageTk

class View:
    """The MVC view for the GUI"""

    root: tk.Tk
    photo_label: tk.Label
    next_button: tk.Button
    word_label: tk.Label
    image_ref: PIL.ImageTk.PhotoImage

    def __init__(self, root: tk.Tk):
        self.root = root

        root.geometry("500x500")

        self.photo_label = tk.Label(root)
        self.next_button = tk.Button(root, text="Next")
        self.word_label = tk.Label(root)

        self.photo_label.pack()
        self.word_label.pack()
        self.next_button.pack()

    def set_image(self, image: PIL.Image.Image, word: str):
        """Changes the image displayed on the GUI"""

        resized = image.resize((250, 250))

        photo = PIL.ImageTk.PhotoImage(resized)

        self.word_label.config(text=word)
        self.photo_label.config(image=photo)
        self.image_ref = photo

    # TODO: Type procedure?
    def on_next(self, proc):
        """Given a procedure, will execute when user presses the next button"""

        self.next_button.config(command=proc)
