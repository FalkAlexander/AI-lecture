class Farberkennung():
    def __get_color_of_pixel(self, argb):
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
        if abs(r - g) < 10 and abs(g - b) < 10 and abs(r - b) < 10 and r > 245:
            return "unbekannt"
        
        if (r > g + 20 and r > b + 20) and (abs(g - b) < 40):
            return "Rot"
        elif (r >= g and r > b) and (g - b > 40):
            return "Gelb"
        elif (abs(r - g) < 30 and abs(g - b) < 30) and abs(r - b) < 30:
            return "Schwarz"
        elif r < g and g < b and r > 170:
            return "Blau"
        
        return "unbekannt"
    
    def get_farbe_dunkel(self):
        if (r > g + 20 and r > b + 20) and abs(g - b) < 40:
            return "Rot"
        elif (r >= g and r > b) and (g - b > 40):
            return "Gelb"
        elif abs(r - g) < 15 and abs(g - b) < 15 and abs(r - b) < 15 and r < 30:
            return "Schwarz"
        elif r < g and g < b and r < 75:
            return "Blau"
        
        return "unbekannt"
        
