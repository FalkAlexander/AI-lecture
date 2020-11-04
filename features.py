from PIL import Image
from farberkennung import Farberkennung
import sys


class Features():
    pixels = NotImplemented

    def __init__(self):
        self.__load_bmp()
    
    def __load_bmp(self):
        if len(sys.argv) <= 1:
            print("No image provided. Exiting...")
            sys.exit()
        
        file_name = sys.argv[1]

        image = Image.open(file_name).convert("RGBA")
        self.pixels = image.load()

        signed_32_rgba_int = self.get_32_signed_rgba(15, 15)
        print("DEBUG | unsigned 32bit integer rgba value: " + str(signed_32_rgba_int))

        fe = Farberkennung()
        farbe = fe.get_color_of_pixel(signed_32_rgba_int)
        print("DEBUG | detected colour: " + farbe)
    
    def __pack_rgba(self, r, g, b, a):
        val = a << 24 | r << 16 | g << 8 | b
        if a & 0x80:
            val -= 0x100000000
        return val
    
    def get_32_signed_rgba(self, x, y):
        return self.__pack_rgba(*self.pixels[x, y])


Features()
