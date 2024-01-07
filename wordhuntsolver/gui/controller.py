"""Contains "Controller" class for GUI"""

import logging
import PIL.Image
from wordhuntsolver.gui.view import View
from wordhuntsolver.ocr_image import OCRParseError
from wordhuntsolver.solver import NoImageError, NoWordListError, Solver

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

        try:
            pathed_images = self._solver.get_pathed_images()
            (word, next_image) = next(pathed_images)
            self._view.set_image(next_image, word)
        except StopIteration:
            self._logger.warning("Words exhausted!")
        except NoWordListError:
            self._logger.error("No word list loaded!")
        except NoImageError:
            self._logger.error("No image loaded!")


    def load_image(self, image_path: str):
        """Loads and processes an image"""

        try:
            image = PIL.Image.open(image_path)

            self._view.set_image(image, "")
            self._solver.set_image(image)
            self._solver.solve()

            self._logger.info("Image loaded.")
        except AttributeError:
            self._logger.error("Image file not found!")
        except NoWordListError:
            self._logger.error("Word list not found!")
        except PIL.UnidentifiedImageError:
            self._logger.error("Invalid image format!")
        except OCRParseError:
            self._logger.error("Unable to parse image!")

    def load_word_list(self, word_list_path):
        """Loads the word list"""

        try:
            with open(word_list_path, encoding="UTF-8") as file:
                self._solver.word_list = file.read().split("\n")

            if self._solver.is_loaded():
                self._solver.solve()

            self._logger.info("Word list loaded.")
        except FileNotFoundError:
            self._logger.error("Word list file not found!")
        except UnicodeDecodeError:
            self._logger.error("Invalid file!")
