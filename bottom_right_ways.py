call_count = 0


def bottom_right_ways(m, n):
    global call_count
    call_count += 1
    if m == 1 or n == 1:
        return 1

    return bottom_right_ways(m-1, n) + bottom_right_ways(m, n-1)


def bottom_right_ways_by_dp(m, n):
    A = [[0] * n] * m
    for i in range(n):
        A[0][i] = 1

    for i in range(m):
        A[i][0] = 1

    for row in range(1, m):
        for col in range(1, n):
            A[row][col] = A[row-1][col] + A[row][col-1]

    return A[m-1][n-1]


if __name__ == "__main__":
    # count = bottom_right_ways(5, 5)
    count = bottom_right_ways_by_dp(5, 5)
    print(count)

    print("{} times func call".format(call_count))
