"""Contains "View" class for GUI"""

from typing import Callable
import tkinter as tk
from tkinter import filedialog
from PIL.Image import Image
from PIL.ImageTk import PhotoImage

class View(tk.Tk):
    """The MVC view for the GUI"""

    root: tk.Tk
    photo_label: tk.Label
    next_button: tk.Button
    word_label: tk.Label
    set_wordlist_button: tk.Button
    set_image_button: tk.Button
    status_label: tk.Label

    status_text: tk.StringVar

    on_next: Callable[[], None] = lambda: None
    on_new_wordlist_path: Callable[[str], None] = lambda _: None
    on_new_image_path: Callable[[str], None] = lambda _: None

    image_ref: PhotoImage

    def __init__(self):
        super().__init__()

        self.geometry("500x500")

        self.status_text = tk.StringVar()

        self.photo_label = tk.Label(self)
        self.word_label = tk.Label(self)
        self.next_button = tk.Button(
            self,
            text="Next",
            command=self._on_next
        )
        self.set_wordlist_button = tk.Button(
            self,
            text="Set word list",
            command=self._on_new_wordlist_path
        )
        self.set_image_button = tk.Button(
            self,
            text="Set image",
            command=self._on_new_image_path
        )
        self.status_label = tk.Label(self, textvariable=self.status_text)

        self.photo_label.pack()
        self.word_label.pack()
        self.status_label.pack()
        self.next_button.pack()
        self.set_wordlist_button.pack()
        self.set_image_button.pack()

    def set_image(self, image: Image, word: str):
        """Changes the image displayed on the GUI"""

        resized = image.resize((250, 250))

        photo = PhotoImage(resized)

        self.word_label.config(text=word)
        self.photo_label.config(image=photo)
        self.image_ref = photo

    def set_status(self, text: str):
        """Sets the status displayed to the user"""

        self.status_text.set(text)

    def clear_status(self):
        """Clears status displayed to user"""

        self.set_status("")

    def _on_next(self):
        self.on_next()

    def _on_new_wordlist_path(self):
        file_path = filedialog.askopenfilename(
            title="Choose a wordlist",
        )
        self.on_new_wordlist_path(file_path)

    def _on_new_image_path(self):
        file_path = filedialog.askopenfilename(
            title="Choose an image",
        )
        self.on_new_image_path(file_path)
