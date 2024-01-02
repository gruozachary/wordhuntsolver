"""Main"""

import sys
import PIL.Image
from wordhuntsolver.solver import Solver

def main():
    """Main function"""

    image_path = sys.argv[1]
    word_list_path = sys.argv[2]

    image = PIL.Image.open(image_path)

    word_list = None
    with open(word_list_path, encoding="UTF-8") as file:
        word_list = file.read().split("\n")

    solver = Solver(image, word_list)

    for path_image in solver.drawn_paths():
        path_image.show()
        input()


if __name__ == "__main__":
    main()
