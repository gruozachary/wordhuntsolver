"""Contains "View" class for GUI"""

from typing import Callable
import tkinter as tk
from tkinter import filedialog
from PIL.Image import Image
from PIL.ImageTk import PhotoImage

class View(tk.Tk):
    """The MVC view for the GUI"""

    _photo_label: tk.Label
    _next_button: tk.Button
    _word_label: tk.Label
    _set_wordlist_button: tk.Button
    _set_image_button: tk.Button
    _status_label: tk.Label

    _status_text: tk.StringVar
    _image_ref: PhotoImage

    on_next: Callable[[], None] = lambda: None
    on_new_wordlist_path: Callable[[str], None] = lambda _: None
    on_new_image_path: Callable[[str], None] = lambda _: None

    def __init__(self):
        super().__init__()

        self._status_text = tk.StringVar()

        self._photo_label = tk.Label(self)
        self._word_label = tk.Label(self)
        self._next_button = tk.Button(
            self,
            text="Next",
            command=self._on_next
        )
        self._set_wordlist_button = tk.Button(
            self,
            text="Set word list",
            command=self._on_new_wordlist_path
        )
        self._set_image_button = tk.Button(
            self,
            text="Set image",
            command=self._on_new_image_path
        )
        self._status_label = tk.Label(self, textvariable=self._status_text)

        self._photo_label.pack()
        self._word_label.pack()
        self._status_label.pack()
        self._next_button.pack()
        self._set_wordlist_button.pack()
        self._set_image_button.pack()

    def set_image(self, image: Image, word: str):
        """Changes the image displayed on the GUI"""

        resized = image.resize((250, 250))

        photo = PhotoImage(resized)

        self._word_label.config(text=word)
        self._photo_label.config(image=photo)
        self._image_ref = photo

    def set_status(self, text: str):
        """Sets the status displayed to the user"""

        self._status_text.set(text)

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
