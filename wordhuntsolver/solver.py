"""Contains the "Solver" class"""

from typing import Generator
from PIL.Image import Image
import practicallan
from wordhuntsolver.ocr_image import OCRImage
from wordhuntsolver.pather import Pather


class Solver:
    """A class that can solve the "Word Hunt" game"""

    _image: Image
    _ocr_image: OCRImage
    _cached_generator: Generator[tuple[str, Image], None, None] | None = None
    _pather: Pather

    word_list: list[str]

    def __init__(self, pather: Pather):
        self._pather = pather

    def set_image(self, image: Image):
        """Sets the image that the solver uses"""

        self._image = image
        self._ocr_image = OCRImage(image)
        self._pather.image = image
        self._pather.character_centres = self._ocr_image.get_character_centres()

    def get_image(self) -> Image:
        """Returns the image being solved"""

        return self._image

    def _generate(self) -> Generator[tuple[str, Image], None, None]:
        word_paths = practicallan.solve(self.word_list, self._ocr_image.get_chars())
        word_paths.sort(key=lambda x: len(x.word))
        word_paths.reverse()

        drawn_words = set()

        def generator():
            for word_path in word_paths:
                if not word_path.word in drawn_words:
                    yield (word_path.word, self._pather.draw_path(word_path))
                    drawn_words.add(word_path.word)

        return generator()

    def is_loaded(self) -> bool:
        """Returns true if an image is loaded"""

        if hasattr(self, "_image"):
            return True
        return False

    def solve(self):
        """Solves the game"""

        self._cached_generator = self._generate()

    def get_pathed_images(self) -> Generator[tuple[str, Image], None, None]:
        """Fetches the images with paths drawn on them"""

        if not self._cached_generator:
            self.solve()

        return self._cached_generator
