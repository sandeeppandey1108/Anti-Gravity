
from PIL import Image, ImageDraw, ImageFont

def create_thumbnail(text):
    img = Image.new('RGB', (1280, 720), color=(0,0,0))
    draw = ImageDraw.Draw(img)
    draw.text((100,300), text, fill=(255,0,0))
    img.save("thumbnail.jpg")
    return "thumbnail.jpg"
