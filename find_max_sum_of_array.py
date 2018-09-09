

def find_max_sum_of_array(input_data):

    if not input_data:
        return 0

    length = len(input_data)
    max_sum = 0
    current_max_sum = 0
    for i in range(length):
        current_max_sum += input_data[i]
        if current_max_sum < 0:
            current_max_sum = 0
        else:
            if current_max_sum > max_sum:
                max_sum = current_max_sum

    return max_sum


if __name__ == "__main__":
    test_input = [34, -50, 42, 14, -5, 86, -20]
    test_max_sum = find_max_sum_of_array(test_input)
    print(test_max_sum)
