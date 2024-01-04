"""Contains the "OCRImage" class"""

from itertools import batched
from PIL.Image import Image
import pytesseract

class OCRImage:
    """Contains functionality to extact data using OCR"""

    _CONFIG = "--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    image: Image

    def __init__(self, image: Image):
        greyscale = image.convert("L")
        self.image = greyscale.point(lambda x: 0 if x < 10 else 255)

    def get_character_centres(self) -> list[list[tuple[int, int]]]:
        """Returns a 2 dimensional array mapping path coordinates to actual image coordinates"""

        data = pytesseract.image_to_boxes(
                self.image,
                output_type=pytesseract.Output.DICT,
                config=self._CONFIG
        )
        _, height = self.image.size

        centres = []
        for i in range(16):
            centre = ((data["left"][i] + data["right"][i]) / 2,
                      height - (data["top"][i] + data["bottom"][i]) / 2)
            centres.append(centre)
        return [list(x) for x in batched(centres, n=4)]

    def get_chars(self) -> list[list[str]]:
        """Returns the characters in the image"""

        raw_string = pytesseract.image_to_string(self.image, config=self._CONFIG)
        return [list(x.replace(" ", "")) for x in raw_string.split("\n") if x != ""]
