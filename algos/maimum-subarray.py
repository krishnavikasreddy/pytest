def maximum_sub_across_array(data, low, high):
    mid = (low + high)/2
    left_sum = float("-inf")
    current_sum = 0
    for x in reversed(range(low, mid + 1)):
        current_sum += data[x]
        if current_sum > left_sum:
            left_sum = current_sum
            left_pos = x
    right_sum = float("-inf")
    current_sum = 0
    for x in range(mid+1, high + 1):
        current_sum += data[x]
        if current_sum > right_sum:
            right_sum = current_sum
            right_pos = x
    return left_pos, right_pos, left_sum + right_sum


def maximum_sub_array(data, low, high):
    if low == high:
        return low, high, data[0]
    else:
        mid = (low + high)/2
        left_min, left_max, left_sum = maximum_sub_array(data, low, mid)
        right_min, right_max, right_sum = maximum_sub_array(data, mid+1, high)
        cross_left, cross_right, cross_sum = maximum_sub_across_array(data,
                                                                      low,
                                                                      high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_min, left_max, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_min, right_max, right_sum
        elif cross_sum >= left_sum and cross_sum >= right_sum:
            return cross_left, cross_right, cross_sum
        return None


def kadane_algorithm(data):
    max_sum_till_now = current_sum = 0
    for item in data:
        current_sum = max(item, current_sum + item)
        max_sum_till_now = max(max_sum_till_now, current_sum)
    return max_sum_till_now


if __name__ == "__main__":
    print maximum_sub_array([1, 2, 3], 0, 2)
    print kadane_algorithm([1, 2, 3])
