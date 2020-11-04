class Farberkennung():
    def get_color_of_pixel(self, argb):
        alpha = (argb >> 24) & 255
        red = (argb >> 16) & 255
        green = (argb >> 8) & 255
        blue = argb & 255

        f = Farbe(red, green, blue)
        luminance = (red * 0.2126 + green * 0.7152 + blue * 0.0722) / 255
    
        if luminance >= 0.05:
            return f.get_farbe_hell()
        else:
            return f.get_farbe_dunkel()    


class Farbe():
    r = NotImplemented
    g = NotImplemented
    b = NotImplemented

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def get_farbe_hell(self):
        if abs(self.r - self.g) < 10 and abs(self.g - self.b) < 10 and abs(self.r - self.b) < 10 and self.r > 245:
            return "Weiß"
        
        if (self.r > self.g + 20 and self.r > self.b + 20) and (abs(self.g - self.b) < 40):
            return "Rot"
        elif (self.r >= self.g and self.r > self.b) and (self.g - self.b > 40):
            return "Gelb"
        elif (abs(self.r - self.g) < 30 and abs(self.g - self.b) < 30) and abs(self.r - self.b) < 30:
            return "Schwarz"
        elif self.r < self.g and self.g < self.b and self.r > 170:
            return "Blau"
        
        return "unbekannt"
    
    def get_farbe_dunkel(self):
        if (self.r > self.g + 20 and self.r > self.b + 20) and abs(self.g - self.b) < 40:
            return "Rot"
        elif (self.r >= self.g and self.r > self.b) and (self.g - self.b > 40):
            return "Gelb"
        elif abs(self.r - self.g) < 15 and abs(self.g - self.b) < 15 and abs(self.r - self.b) < 15 and self.r < 30:
            return "Schwarz"
        elif self.r < self.g and self.g < self.b and self.r < 75:
            return "Blau"
        
        return "unbekannt"
        
