"""Contains "Controller" class for GUI"""

from typing import Generator

import PIL.Image

from wordhuntsolver.gui.view import View
from wordhuntsolver.solver import Solver

class Controller:
    """The MVC controller for the GUI"""

    solver: Solver
    view: View
    drawn_images: Generator[PIL.Image.Image, None, None]

    def __init__(self, solver: Solver, view: View):
        self.solver = solver
        self.view = view
        self.drawn_images = solver.drawn_paths()

        self.view.set_image(self.solver.image)
        self.view.on_next(self._load_next)

    def _load_next(self):
        next_image = next(self.drawn_images)

        self.view.set_image(next_image)
