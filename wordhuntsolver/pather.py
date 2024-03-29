"""Contains the "Pather" class"""

from itertools import pairwise
from practicallan import WordPath

from PIL.Image import Image
from PIL.ImageDraw import ImageDraw

class Pather:
    """Draws paths over the image of the game"""

    character_centres: list[list[tuple[int, int]]]
    image: Image

    def draw_path(self, path: WordPath) -> Image:
        """Returns an image with a path drawn over it"""

        image = self.image.copy()
        draw = ImageDraw(image)

        for (x_0, y_0), (x_1, y_1) in pairwise(path.cartesian_path):
            draw.line([self.character_centres[y_0][x_0],
                       self.character_centres[y_1][x_1]], width=5, fill="red")

        return image
