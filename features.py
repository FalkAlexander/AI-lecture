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

        self.write_feature_file_start()
        self.count_pixel_colors()

    def __pack_rgba(self, r, g, b, a):
        val = a << 24 | r << 16 | g << 8 | b
        if a & 0x80:
            val -= 0x100000000
        return val
    
    def get_32_signed_rgba(self, x, y):
        return self.__pack_rgba(*self.pixels[x, y])
    
    def __count(self, area):
        fe = Farberkennung()

        red_count = 0
        yellow_count = 0
        blue_count = 0
        black_count = 0
        white_count = 0
        unknown_count = 0

        x_start_bound = area[0][0]
        x_end_bound = area[0][1]
        y_start_bound = area[1][0]
        y_end_bound = area[1][1]

        for x in range(x_start_bound, x_end_bound):
            for y in range(y_start_bound, y_end_bound):
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

        colour_list = {}
        colour_list["Rot"] = red_count
        colour_list["Blau"] = blue_count
        colour_list["Schwarz"] = black_count
        colour_list["Weiß"] = white_count
        colour_list["Unknown"] = unknown_count

        sorted_colour_list = sorted(colour_list.items(), key=lambda x: x[1])

        return sorted_colour_list

    def count_pixel_colors(self):
        width, height = self.image.size

        x_grid = int(width / 3)
        y_grid = int(height / 3)

        x_first = [0, x_grid]
        x_second = [x_grid + 1, x_grid * 2]
        x_third = [x_grid * 2 + 1, width]
        y_first = [0, y_grid]
        y_second = [y_grid + 1, y_grid * 2]
        y_third = [y_grid * 2 + 1, height]

        top_left = [x_first, y_first]
        top_middle = [x_second, y_first]
        top_right = [x_third, y_first]
        middle_left = [x_first, y_second]
        middle_middle = [x_second, y_second]
        middle_right = [x_third, y_second]
        bottom_left = [x_first, y_third]
        bottom_middle = [x_second, y_third]
        bottom_right = [x_third, y_third]

        areas = {}
        areas["top_left"] = top_left
        areas["top_middle"] = top_middle
        areas["top_right"] = top_right
        areas["middle_left"] = middle_left
        areas["middle_middle"] = middle_middle
        areas["middle_right"] = middle_right
        areas["bottom_left"] = bottom_left
        areas["bottom_middle"] = bottom_middle
        areas["bottom_right"] = bottom_right
        print(areas)

        for area in areas:
            areas[area] = self.__count(areas[area])
        self.write_features_to_file(areas)

    def write_feature_file_start(self):
        file_name = "features_" + sys.argv[1] + ".txt"

        features = ("=================== " + sys.argv[1] + " ===================\n")

        f = open(file_name, "a+", encoding="utf-8")
        f.write(features)
        f.close()
    
    def write_features_to_file(self, sorted_colour_list):
        file_name = "features_" + sys.argv[1] + ".txt"

        features = (str(sorted_colour_list) + "\n")

        f = open(file_name, "a+", encoding="utf-8")
        f.write(features)
        f.close()


Features()
