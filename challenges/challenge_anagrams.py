def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return "", "", False

    first_sorted = merge_sort(list(first_string.lower()))
    second_sorted = merge_sort(list(second_string.lower()))

    return (
        "".join(first_sorted),
        "".join(second_sorted),
        first_sorted == second_sorted
    )
