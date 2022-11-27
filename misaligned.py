
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)
def getColorCode(major_color,minor_color):
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    colorCode = {}
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            colorCode[str({major} | {minor})] = i * 5 + j
    return colorCode[str({major_color} | {minor_color})]

result = print_color_map()
assert(result == 25)
assert(getColorCode("Red","Orange") == 7)
assert(getColorCode("Violet","Green") == 21)
print("All is well (maybe!)\n")
