from PIL import Image, ImageDraw, ImageFont
import random
import os
from numpy.random.mtrand import Sequence
# import pdb


class MemeEngine():

    def __init__(self, output_path: str):
        self.path = output_path

    def make_meme(self, img_path, text=None, author=None, width=500) -> str:
        """Create a Image With Text that includes the body and author

        Arguments:
            in_path {str} -- the file location for the input image.
            test {str} -- text information that is draw on the image. reference as the body text
            author {str} -- author text that is draw on the image.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        # pdb.set_trace(header ="Meme Engine")
        image = Image.open(img_path)

        ratio = width / float(image.size[0])
        height = int(ratio * float(image.size[1]))
        image = image.resize((width, height), Image.Resampling.NEAREST)

        if text is not None or author is not None:
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('./fonts/Roboto-Regular.ttf', size=40)
            draw.text((random.randint(0, 50),
                       random.randint(0, 50)),
                      f'{text} {author}',
                      font=font,
                      fill='white')

        image.save(self.path)

        return f'{self.path}'
