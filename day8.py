from functools import reduce
digits = open("input/day8.txt").readline()

print("A:")

width = 25   
height = 6
layer_size = width * height
layers = [digits[left: left + layer_size] 
            for left in range(0, len(digits) - 1, layer_size)]

least_zeros = lambda a, b: a if a.count('0') < b.count('0') else b
minLayer = reduce(least_zeros, layers) 

print(minLayer.count('1') * minLayer.count('2'))

print("B:")

# Go through layers and print visible pixels
color = lambda x: 'X' if x == '1' else ' '
new_layer = ""
for h in range(height):
    for w in range(width):
        layer_level = 0
        pixel = '2' 
        while (pixel == '2'): # layer invisible - look at next
            pixel = layers[layer_level][h * width + w]
            layer_level += 1
        print(color(pixel), end='')
    print()
