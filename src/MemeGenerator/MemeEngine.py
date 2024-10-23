from PIL import Image, ImageDraw, ImageFont
import random

from numpy.random.mtrand import Sequence


class MemeEngine:

    def __init__(self, output_path: str):
        self.path = output_path

    def make_meme(self, img_path, text=None, author=None, width=500) -> str:

        image = Image.open(img_path)

        if width is not None:
            ratio = width / float(image.size[0])
            height = int(ratio * float(image.size[1]))
            image = image.resize((width, height), Image.Resampling.NEAREST)

        if text is not None or author is not None:
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('veranda.tff', size=40)
            draw.text((random.randint(0,50),
                       random.randint(0,50)),
                      f'{text} {author}',
                       font=font,
                       fill='white'
                      )

        image.save(self.path)

        return f'{self.path}'




