"""Main"""

import sys
import tomllib
import tkinter as tk
import PIL.Image
import pytesseract
from wordhuntsolver.gui.controller import Controller
from wordhuntsolver.gui.view import View
from wordhuntsolver.pather import Pather
from wordhuntsolver.solver import Solver

def main():
    """Main function"""

    image_path = sys.argv[1]
    word_list_path = sys.argv[2]

    image = PIL.Image.open(image_path)

    word_list = None
    with open(word_list_path, encoding="UTF-8") as file:
        word_list = file.read().split("\n")

    with open("config.toml", "rb") as file:
        data = tomllib.load(file)
        pytesseract.pytesseract.tesseract_cmd = data["tesseract"]["command"]

    root = tk.Tk()

    view = View(root)
    solver = Solver(Pather())
    solver.set_image(image)
    solver.word_list = word_list

    Controller(solver, view)

    root.mainloop()


if __name__ == "__main__":
    main()
