from PIL import Image, ImageFont, ImageDraw
import os

w = 500
h = 100

text = "SALUT"
output_folder = "output"

img = Image.new('RGB', (w, h), "black")  # create a new black image
pixels = img.load()  # create the pixel map

font = ImageFont.truetype("./led.ttf", size=42)
draw = ImageDraw.Draw(img)


def add_text_padding(text):
    padding = 5
    padding_char = "_"
    return padding_char * padding + text + padding_char * padding


text = add_text_padding(text)

for t in range(len(text)):
    temp = img.copy()
    draw = ImageDraw.Draw(temp)

    # shift algorithm that is not that good
    text = text[t:] + text[:t]

    draw.text((0, h / 2 - len(text) // 2), text, (255, 255, 255), font=font)
    temp.show(text)

    temp.save(output_folder + "/" + "%s.png" % t)

# use imagemagick to create gif
os.system("convert -delay 20 -loop 0 %s/*.png %s/output.gif" % (output_folder, output_folder))
