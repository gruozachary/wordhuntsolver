"""Contains the "Solver" class"""

from typing import Generator
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

    def drawn_paths(self) -> Generator[tuple[str, PIL.Image.Image], None, None]:
        """A generator that yields the drawn path images"""

        word_paths = practicallan.solve(self.word_list, self.ocr_image.get_chars())
        word_paths.sort(key=lambda x: len(x.word))
        word_paths.reverse()

        drawn_words = set()
        for word_path in word_paths:
            if not word_path.word in drawn_words:
                yield (word_path.word, self.pather.draw_path(word_path))
                drawn_words.add(word_path.word)
