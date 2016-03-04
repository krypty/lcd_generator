from PIL import Image, ImageFont, ImageDraw
import os
import datetime


class LCDGenerator:

    def __init__(self, output_folder, background_color_hex_code, text_color_hex_code):
        self.output_folder = output_folder
        self.results_folder = 'results'
        self.back_color = background_color_hex_code
        self.text_color = text_color_hex_code
        self.size = 96
        self.font = ImageFont.truetype("resources/led.ttf", size=self.size)
        self.delay = 20
        self.nb_max_chars_displayed = 15
        self.nb_empty = 5

    def set_size(self, size):
        size = size if size > 0 else 96
        self.size = size
        self.font = ImageFont.truetype("resources/led.ttf", size=self.size)

    def set_delay(self, delay):
        delay = delay if delay > 0 else 20
        self.delay = delay

    def set_nb_empty(self, nb_empty):
        nb_empty = nb_empty if nb_empty >= 0 else 5
        self.nb_empty = nb_empty

    def set_max_chars_displayed(self, max_displayed):
        max_displayed = max_displayed if max_displayed > 0 else 15
        self.nb_max_chars_displayed = max_displayed

    def format_name(self, index):
        str_index = str(index)
        if index < 10:
            str_index = "00%d" % index
        elif index >= 10 and index < 100:
            str_index = "0%d" % index
        return str_index

    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def clean_output_folder(self):
        for the_file in os.listdir(self.output_folder):
            file_path = os.path.join(self.output_folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except:
                continue

    def generate_gif_custom_colors(self, text, back_color, text_color):
        nb_chars_displayed_max = len(text) if len(text) < self.nb_max_chars_displayed else self.nb_max_chars_displayed
        w = self.size * nb_chars_displayed_max
        h = int(self.size + self.size / 2)

        img = Image.new('RGB', (w, h), back_color)  # create a new black image

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        if not os.path.exists(self.results_folder):
            os.makedirs(self.results_folder)

        for t in range(2 * self.nb_empty + len(text)):
            temp = img.copy()
            draw = ImageDraw.Draw(temp)

            draw.text(((nb_chars_displayed_max + self.nb_empty - t) * self.size, h / 2 - self.size / 2), text, self.hex_to_rgb(text_color), font=self.font)

            ts = self.format_name(t)
            temp.save(self.output_folder + "/" + "%s.png" % ts)

        # use imagemagick to create gif
        os.system("convert -delay %d -loop 0 %s/*.png %s/output_%s.gif" %
                  (self.delay, self.output_folder, self.results_folder, datetime.datetime.now().strftime("%I:%M:%S%p_%b-%d-%Y")))

    def generate_gif(self, text):
        self.generate_gif_custom_colors(text, self.back_color, self.text_color)

    def get_gif_file(self):
        pass

