


from PIL import Image, ImageDraw, ImageFont
import time


def label_image(cam, img_path, out_path):
    """Adds a text label onto a jpeg image"""
    text = '{0}  -  {1}'.format(cam['title'], time.strftime("%d.%m.%Y %H:%M", time.localtime()))
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("webcamuploader/font/OpenSans-Semibold.ttf", 14)

    draw.text((5, 5), text, (255, 255, 255, 127), font=font)

    img.save(out_path)