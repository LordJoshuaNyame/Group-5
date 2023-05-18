def height_category (height):
 if height > 6.0:
    return ("Long")
 elif height >= 5.6 and height <= 5.9:
    return ("Tall")
 elif height >= 4.5 and height <= 5.5:
    return ("Medium")
 elif height >= 2.5 and height <= 4.5:
    return ("Short")
 else:
    return ("Dwarf")

