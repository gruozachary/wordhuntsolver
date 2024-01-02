"""Contains the "Solver" class"""

import PIL.Image
import practicallan
from wordhuntsolver.ocr_image import OCRImage
from wordhuntsolver.pather import Pather


class Solver:
    """A class that can solve the "Word Hunt" game"""

    image: PIL.Image.Image
    word_list: list[str]
    pather: Pather
    ocr_image: OCRImage

    def __init__(self, image: PIL.Image.Image, word_list: list[str]):
        self.image = image
        self.word_list = word_list
        self.ocr_image = OCRImage(image)
        self.pather = Pather(self.ocr_image.get_character_centres(), image)

    # TODO: type hint generator?
    def drawn_paths(self):
        """A generator that yields the drawn path images"""

        word_paths = practicallan.solve(self.word_list, self.ocr_image.get_chars())
        word_paths.sort(key=lambda x: len(x.word))
        word_paths.reverse()

        for word_path in word_paths:
            yield self.pather.draw_path(word_path)
