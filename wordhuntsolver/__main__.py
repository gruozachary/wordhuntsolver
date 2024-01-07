"""Main"""

import tomllib
import pytesseract
from wordhuntsolver.gui.controller import Controller
from wordhuntsolver.gui.view import View
from wordhuntsolver.pather import Pather
from wordhuntsolver.solver import Solver

config = {
    "tesseract": {
        "command": "tesseract"
    },
    "word_list": {
        "default_path": "word_list.txt"
    }
}

def main():
    """Main function"""

    view = View()
    solver = Solver(Pather())

    controller = Controller(solver, view)

    with open("config.toml", "rb") as file:
        config.update(tomllib.load(file))

        pytesseract.pytesseract.tesseract_cmd = config["tesseract"]["command"]
        controller.load_word_list(config["word_list"]["default_path"])

    view.mainloop()


if __name__ == "__main__":
    main()
