#!/usr/bin/env python
"""Takes an image as input, and returns an ascii string
that resembles the input image.

Returns:
    string: ascii characters
"""

from PIL import Image

IM = Image.open("./photos/bart.png").convert('RGB')

WIDTH, HEIGHT = IM.size
CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def generate_pixel_array(image):
    """generate_pixel_array takes in an image file, and returns a two-diemensional
    array of tuples. These tuples contain three numbers corresponding to the RBG
    values of the pixel.

    Args:
        object: PIL.Image

    Returns:
        list: two-diemensional list of tuples.
    """
    full_array = []
    y = 1
    while y < HEIGHT:
        x = 1
        line_array = []
        while x < WIDTH:
            line_array.append(image.getpixel((x, y)))
            x += 1
        y += 1
        full_array.append(line_array)
    return full_array

def construct_brightness_matrix(rgb_array):
    """construct_brightness_matrix [summary]

    Args:
        rgb_array (list): two-dimensional RGB pixel list.

    Returns:
        list: two-dimensional list of pixel brightness levels.
    """
    brightness_matrix = []
    for y in rgb_array:
        line_brightness = []
        for x in y:
            line_brightness.append(convert_rgb_to_brightness(x[0], x[1], x[2]))
        brightness_matrix.append(line_brightness)
    return brightness_matrix

def convert_rgb_to_brightness(red, green, blue):
    """convert_rgb_to_brightness takes in RGB values of a pixel and converts them to
    an equivalent brightness constant from 0-255.

    Args:
        red (int): red colour constant
        green (int): green colour constant
        blue (int: blue colour constant

    Returns:
        int: brightness constant
    """
    return round((red * 0.21) + (green * 0.72) + (blue * 0.07))    

def construct_ascii_array(brightness_matrix):
    """construct_ascii_array converts a two-dimensional list to equivalent ASCII
    characters from pixel brightness levels.

    Args:
        brightness_matrix (list): two-dimensional list of pixel brightness levels.

    Returns:
        list: two-dimensional list of ASCII characters.
    """
    ascii_list = []
    for y in brightness_matrix:
        line_array = [ round(x / 5) for x in y ]
        ascii_line = [ CHARS[num] for num in line_array ]
        ascii_list.append(ascii_line)
    return ascii_list

def splice_ascii_list(ascii_list):
    """splice_ascii_list joins lines of ASCII characters into complete string.

    Args:
        ascii_list (list): two-dimensional list of ASCII characters.

    Returns:
        string: final picture string of ASCII characters.
    """
    picture_string = ''
    for y in ascii_list:
        picture_string = picture_string + "".join(y) + "\n"
    return picture_string


picture = generate_pixel_array(IM)
picture = construct_brightness_matrix(picture)
print("Successfully constructed brightness matrix!")
print(f"Brightness matrix size {WIDTH} x {HEIGHT}")
picture = construct_ascii_array(picture)
picture = splice_ascii_list(picture)

print(picture)
