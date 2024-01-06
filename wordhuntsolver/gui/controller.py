"""Contains "Controller" class for GUI"""

import logging
import PIL.Image
from wordhuntsolver.gui.view import View
from wordhuntsolver.solver import Solver

class Controller:
    """The MVC controller for the GUI"""

    _solver: Solver
    _view: View

    _logger: logging.Logger

    def __init__(self, solver: Solver, view: View):
        self._solver = solver
        self._view = view

        self._view.on_next = self._load_next
        self._view.on_new_image_path = self.load_image
        self._view.on_new_wordlist_path = self.load_word_list

        self._logger = logging.getLogger("View")

    def _load_next(self):
        pathed_images = self._solver.get_pathed_images()

        (word, next_image) = next(pathed_images)

        self._view.set_image(next_image, word)

    def load_image(self, image_path: str):
        """Loads and processes an image"""

        try:
            image = PIL.Image.open(image_path)

            self._view.set_image(image, "")
            self._solver.set_image(image)
            self._solver.solve()

            self._logger.info("Image loaded.")
        except AttributeError:
            self._logger.error("File not found!")
        except PIL.UnidentifiedImageError:
            self._logger.error("Invalid image!")

    def load_word_list(self, word_list_path):
        """Loads the word list"""

        try:
            with open(word_list_path, encoding="UTF-8") as file:
                self._solver.word_list = file.read().split("\n")

            self._logger.info("Word list loaded.")
        except FileNotFoundError:
            self._logger.error("File not found!")
        except UnicodeDecodeError:
            self._logger.error("Invalid file!")
