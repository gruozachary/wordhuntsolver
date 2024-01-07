"""Main"""

import sys
import tomllib
import pytesseract
from wordhuntsolver.gui.controller import Controller
from wordhuntsolver.gui.view import View
from wordhuntsolver.pather import Pather
from wordhuntsolver.solver import Solver

def main():
    """Main function"""

    with open("config.toml", "rb") as file:
        data = tomllib.load(file)
        pytesseract.pytesseract.tesseract_cmd = data["tesseract"]["command"]

    view = View()
    solver = Solver(Pather())

    controller = Controller(solver, view)

    view.mainloop()


if __name__ == "__main__":
    main()
