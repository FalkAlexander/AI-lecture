from PIL import Image
from farberkennung import Farberkennung
import sys


class Features():
    image = NotImplemented
    pixels = NotImplemented

    def __init__(self):
        self.__load_bmp()
    
    def __load_bmp(self):
        if len(sys.argv) <= 1:
            print("No image provided. Exiting...")
            sys.exit()
        
        file_name = sys.argv[1]

        self.image = Image.open(file_name).convert("RGBA")
        self.pixels = self.image.load()

        signed_32_rgba_int = self.get_32_signed_rgba(15, 15)
        print("DEBUG | unsigned 32bit integer rgba value: " + str(signed_32_rgba_int))

        fe = Farberkennung()
        farbe = fe.get_color_of_pixel(signed_32_rgba_int)
        print("DEBUG | detected colour: " + farbe)

        self.count_pixel_colors()

    def __pack_rgba(self, r, g, b, a):
        val = a << 24 | r << 16 | g << 8 | b
        if a & 0x80:
            val -= 0x100000000
        return val
    
    def get_32_signed_rgba(self, x, y):
        return self.__pack_rgba(*self.pixels[x, y])
    
    def count_pixel_colors(self):
        fe = Farberkennung()

        red_count = 0
        yellow_count = 0
        blue_count = 0
        black_count = 0
        white_count = 0
        unknown_count = 0
        width, height = self.image.size
        for x in range(width):
            for y in range(height):
                value = fe.get_color_of_pixel(self.get_32_signed_rgba(x, y))
                if value == "Weiß":
                    white_count +=1
                elif value == "Rot":
                    red_count += 1
                elif value == "Gelb":
                    yellow_count += 1
                elif value == "Schwarz":
                    black_count += 1
                elif value == "Blau":
                    blue_count += 1
                elif value == "unknown":
                    unknown_count +=1

        print("Rot: " + str(red_count))
        print("Gelb: " + str(yellow_count))
        print("Blau: " + str(blue_count))
        print("Schwarz: " + str(black_count))
        print("Weiß: " + str(white_count))
        print("Unknown: " + str(unknown_count))

        colour_list = {}
        colour_list["Rot"] = red_count
        colour_list["Blau"] = blue_count
        colour_list["Schwarz"] = black_count
        colour_list["Weiß"] = white_count
        colour_list["Unknown"] = unknown_count

        sorted_colour_list = sorted(colour_list.items(), key=lambda x: x[1])

        frst_colour = sorted_colour_list[-1][0]
        scnd_colour = sorted_colour_list[-2][0]
        thrd_colour = sorted_colour_list[-3][0]

        self.write_features_to_file(frst_colour, scnd_colour, thrd_colour)
    
    def write_features_to_file(self, frst_colour, scnd_colour, thrd_colour):
        file_name = "features_" + sys.argv[1] + ".txt"

        features = (""
        "============== FARBANZAHL ==============\n"
        "----------- Alle Koordinaten -----------\n"
        "Häufigste Farbe: " + frst_colour + " \n"
        "Zweithäufigste Farbe: " + scnd_colour + " \n"
        "Dritthäufigste Farbe: " + thrd_colour + " \n")

        f = open(file_name, "w+", encoding="utf-8")
        f.write(features)
        f.close()


Features()
