major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
colorCode = {}
def print_color_map():
    output_string = ""
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            colorCode[str({major} | {minor})] = i * 5 + j
            output_string += f'{i * 5 + j} | {major} | {minor}'
            output_string += '\n'
    return len(major_colors) * len(minor_colors) , output_string

def find_indexes(find_element, full_string):
    indexes_list = []
    for index , each_char in enumerate(full_string):
        if each_char == find_element:
            indexes_list.append(index)
    return indexes_list

result , output_string = print_color_map()
# Test result length
assert(result == 25)

# Test allignment
output_list = output_string.splitlines()
reference_index_list = find_indexes('|',output_list[0])
for each_line in output_list:
    assert(find_indexes('|',each_line) == reference_index_list)

# Test colorcode Match as per wiki page
assert(colorCode[str({"Red"} | {"Orange"})] == 7)
assert(colorCode[str({"Violet"} | {"Green"})] == 23)


print("All is well (maybe!)\n")
