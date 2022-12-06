major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
colorCode = {}


def get_color_code(index1, index2):
    return index1 * 5 + index2
    
def format_color_code(color_code, major_color, minor_color):
    formatted_string = f'{color_code}'+' '*(3 - len(str(color_code))) + f'| {major_color}' + ' '*(7 - len(major_color))+f'| {minor_color}'
    return formatted_string

def get_output_string():
    output_string = ""
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors,start=1):
            color_code = get_color_code(i,j)
            colorCode[str({major} | {minor})] = color_code
            output_string += format_color_code(color_code,major,minor)
            output_string += '\n'
    return len(major_colors) * len(minor_colors) , output_string

def print_color_map(formatted_string):
    print(formatted_string)

def find_indexes(find_element, full_string):
    indexes_list = []
    for index , each_char in enumerate(full_string):
        if each_char == find_element:
            indexes_list.append(index)
    return indexes_list

result , output_string = get_output_string()
print_color_map(output_string)
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
