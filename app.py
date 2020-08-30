from PIL import Image

im = Image.open("./photos/ghandi.jpg").convert('RGB')

width, height = im.size

def generate_pixel_array():
    full_array = []
    h = 1
    while h < height:
        w = 1
        line_array = []
        while w < width:
            line_array.append(im.getpixel((w, 10)))
            w += 1
        h += 1
        full_array.append(line_array)
    return full_array

array = generate_pixel_array()
print(array)