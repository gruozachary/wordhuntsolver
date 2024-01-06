"""Contains "View" class for GUI"""

from typing import Callable
import tkinter as tk
from tkinter import filedialog
import logging
from PIL.Image import Image
from PIL.ImageTk import PhotoImage

class LabelHandler(tk.Label, logging.Handler):
    def __init__(self, *args, **kwargs):
        logging.Handler.__init__(self, level=logging.DEBUG)
        tk.Label.__init__(self, *args, **kwargs)

    def emit(self, record: logging.LogRecord):
        formatted_record = self.format(record)
        match record.levelno:
            case 20: self["fg"] = "green"
            case 30: self["fg"] = "yellow"
            case 40: self["fg"] = "red"
        self["text"] = formatted_record


class View(tk.Tk):
    """The MVC view for the GUI"""

    _photo_label: tk.Label
    _next_button: tk.Button
    _word_label: tk.Label
    _set_wordlist_button: tk.Button
    _set_image_button: tk.Button
    _status_label: LabelHandler

    _image_ref: PhotoImage

    on_next: Callable[[], None] = lambda: None
    on_new_wordlist_path: Callable[[str], None] = lambda _: None
    on_new_image_path: Callable[[str], None] = lambda _: None

    def __init__(self):
        super().__init__()

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
        self._status_label = LabelHandler(self)

        self._photo_label.grid(column=1, row=0, rowspan=3)
        self._word_label.grid(column=1, row=3)
        self._status_label.grid(column=1, row=4)
        self._next_button.grid(column=0, row=0, sticky="ew")
        self._set_wordlist_button.grid(column=0, row=1, sticky="ew")
        self._set_image_button.grid(column=0, row=2, sticky="ew")

        self._init_logger()

    def _init_logger(self):
        logger = logging.getLogger("View")
        logger.setLevel(logging.INFO)
        logger.addHandler(self._status_label)

    def set_image(self, image: Image, word: str):
        """Changes the image displayed on the GUI"""

        resized = image.resize((250, 250))

        photo = PhotoImage(resized)

        self._word_label.config(text=word)
        self._photo_label.config(image=photo)
        self._image_ref = photo

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
