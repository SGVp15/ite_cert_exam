from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Contact
from config import TEMPLATE_FOLDER


def create_png(contact: Contact):
    img = Image.open(f'{TEMPLATE_FOLDER}/{contact.template}')

    image_draw = ImageDraw.Draw(img)

    my_font = ImageFont.truetype('./fonts/Geometria/geometria_light.otf', 70)
    image_draw.text((647, 1220),
                    f'№ {contact.number:06}   {contact.date_exam}', font=my_font, fill=(16, 21, 84))

    my_font = ImageFont.truetype('./fonts/Rubik/Rubik-Regular.ttf', 115)
    image_draw.text((round(0.59 * img.width), 1550),
                    f'{contact.name_rus}', font=my_font, fill=(16, 21, 84),
                    anchor='mm')

    my_font = ImageFont.truetype('./fonts/Rubik/Rubik-Regular.ttf', 70)
    image_draw.text((round(0.59 * img.width), 1700),
                    f'{contact.name_eng}', font=my_font, fill=(16, 21, 84), anchor='mm')

    img.save(contact.file_out_png)
