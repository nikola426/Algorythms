from sys import maxsize


def find_max_under_boundary(arr, boundary):
    current_max = -maxsize - 1

    for elem in arr:
        if elem < boundary:
            current_max = max(current_max, elem)

    return current_max


def find_top_elements(arr, number_of_elements):
    top_list = [None for _ in range(number_of_elements)]
    previous_max = maxsize

    for i in range(number_of_elements):
        current_max = find_max_under_boundary(arr, previous_max)
        previous_max = current_max
        top_list[i] = current_max

    return top_list

nums = [0, 8, 0, 2, 9, -2]

print(find_top_elements(nums, 3))