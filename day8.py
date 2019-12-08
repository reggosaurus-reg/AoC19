digits = open("input/day8.txt").readline()

print("A:")

width = 25   
height = 6
layer_size = width * height
layers = []

# Divide digits into (flat) layers
while (len(digits) >= layer_size):
    layers.append(digits[:layer_size])
    digits = digits[layer_size:]

# Find layer with least 0's
minLayer = -1
currentMin = float('inf')
for layer in layers:
    num = layer.count('0')
    if num < currentMin:
        currentMin = num
        minLayer = layer 

print(minLayer.count('1') * minLayer.count('2'))


print("B:")

# Go through layers and find visible pixels
new_layer = ""
for pixel_pos in range(layer_size):
    layer_level = 0
    pixel = '2' 
    while (pixel == '2'):
        pixel = layers[layer_level][pixel_pos]
        layer_level += 1
    new_layer += pixel


new_layer = new_layer.replace("1", 'X')
new_layer = new_layer.replace("0", ' ')
for i in range(height):
    print(new_layer[i * width: (i + 1) * width])
