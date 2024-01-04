"""Contains "Controller" class for GUI"""

import PIL.Image

from wordhuntsolver.gui.view import View
from wordhuntsolver.solver import Solver

class Controller:
    """The MVC controller for the GUI"""

    _solver: Solver
    _view: View

    def __init__(self, solver: Solver, view: View):
        self._solver = solver
        self._view = view

        self._view.on_next(self._load_next)

    def _load_next(self):
        pathed_images = self._solver.get_pathed_images()

        (word, next_image) = next(pathed_images)

        self._view.set_image(next_image, word)

    def load_image(self, image_path: str):
        """Loads and processes an image"""

        image = PIL.Image.open(image_path)

        self._view.set_image(image, "")
        self._solver.set_image(image)
        self._solver.solve()

    def load_word_list(self, word_list_path):
        """Loads the word list"""

        with open(word_list_path, encoding="UTF-8") as file:
            self._solver.word_list = file.read().split("\n")
