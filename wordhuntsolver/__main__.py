"""Main"""

import sys
import tomllib
import tkinter as tk
import pytesseract
from wordhuntsolver.gui.controller import Controller
from wordhuntsolver.gui.view import View
from wordhuntsolver.pather import Pather
from wordhuntsolver.solver import Solver

def main():
    """Main function"""

    image_path = sys.argv[1]
    word_list_path = sys.argv[2]

    with open("config.toml", "rb") as file:
        data = tomllib.load(file)
        pytesseract.pytesseract.tesseract_cmd = data["tesseract"]["command"]

    root = tk.Tk()

    view = View(root)
    solver = Solver(Pather())

    controller = Controller(solver, view)
    controller.load_word_list(word_list_path)
    controller.load_image(image_path)

    root.mainloop()


if __name__ == "__main__":
    main()
