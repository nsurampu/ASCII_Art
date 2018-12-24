from PIL import Image
import numpy
import math

def avg_pixel(pixel):
    some = (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3
    return some

def max_min_pixel(pixel):
    some = (max(pixel[0], pixel[1], pixel[2]) + min(pixel[0], pixel[1], pixel[2])) / 2
    return some

def lumin_pixel(pixel):
    some = 0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]
    return some

im = Image.open(input("Enter image path: "))
# im = Image.open("firefox.png")
# im = Image.open("image1.jpg")
# im = Image.open("image1.jpg").convert("L")
# print(im.format, im.size, im.mode)
# im.show()
ascii_table = ['`', '^', '"', ':', ';', 'I', 'l', '!', 'i', '~', '+', '_', '-', '?', ']',
'[', '}', '{', '1', ')', '(', '|', '\\', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X',
'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']
size = (128, 128)
im.thumbnail(size)
im_array = numpy.array(im)
im_array = im_array
ln = int(numpy.shape(im_array)[0])
wd = int(numpy.shape(im_array)[1])
ascii_im = [[0 for _ in range(wd)] for _ in range(ln)]
line_count = 0
pixel_count = 0
# print(numpy.shape(im_array))

for line in im_array:
    print("--> Processing pixel array: " + str((line_count + 1)))
    for pixel in line:
        # print(pixel[0], pixel[1], pixel[2])
        some = lumin_pixel(pixel)
        some = (some * 64) / 255
        some = int(round(some))
        ascii_im[line_count][pixel_count] = ascii_table[some]
        pixel_count = pixel_count + 1
    pixel_count = 0
    line_count = line_count + 1

# print(len(ascii_im[0]))
# new_im1 = Image.fromarray(im_array)
# new_im1.show()
for line in ascii_im:
    for pixel in line:
        print(pixel, end='')
    print("")
