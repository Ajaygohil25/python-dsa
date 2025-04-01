def largestElement(arr, max_element=float('-inf')):
    for element in arr:
        if isinstance(element, list):
            max_element= largestElement(element,max_element)
        else:
            if element > max_element:
                max_element= element
    return max_element

nested_array = [[-3, -4, -58], [709, -8, [15, -999, [11,-2, [1000, 700]]]], [-111, -2]]
large = largestElement(nested_array)
print(f"this is large element in array : {large}")
