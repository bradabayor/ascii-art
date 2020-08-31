#!/usr/bin/env python

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
            line_array.append(im.getpixel((w, h)))
            w += 1
        h += 1
        full_array.append(line_array)
    return full_array

def construct_brightness_matrix(rgb_array):
    new_array = []
    for h in rgb_array:
        line_array = []
        for w in h:
            red = w[0] * 0.21
            green = w[1] * 0.72
            blue = w[2] * 0.07
            lum = red + green + blue
            w = round(lum)
            line_array.append(w)
        new_array.append(line_array)
    print("Successfully constructed brightness matrix!")
    print(f"Brightness matrix size {width} x {height}")
    return new_array



rgb_array = generate_pixel_array()
lum_array = construct_brightness_matrix(rgb_array)

#print(rgb_array)

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

final_array = []
for h in lum_array:
    line_array = [ round(w / 5) for w in h ]
    ascii_array = [ chars[w] for w in line_array ]
    final_array.append(ascii_array)

print(final_array)
