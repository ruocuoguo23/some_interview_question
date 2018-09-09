class FindAddList:

    def find_add_list(self, input_list, k, add_list):

        if not input_list:
            return False

        if input_list[0] == k:
            add_list.append(input_list[0])
            return True

        if input_list[0] > k:
            return self.find_add_list(input_list[1:], k, add_list)
        else:
            result_with_add_current = self.find_add_list(input_list[1:], k-input_list[0], add_list)
            result_with_no_add = self.find_add_list(input_list[1:], k, add_list)
            if result_with_add_current:
                add_list.append(input_list[0])

            return result_with_add_current | result_with_no_add


def subset_sum(nums, k):
    A = [[None for _ in range(k + 1)] for _ in range(len(nums) + 1)]

    for i in range(len(nums) + 1):
        A[i][0] = []

    for i in range(1, len(nums) + 1):
        for j in range(1, k + 1):
            last = nums[i - 1]
            if last > j:
                A[i][j] = A[i - 1][j]
            else:
                if A[i - 1][j] is not None:
                    A[i][j] = A[i - 1][j]
                elif A[i - 1][j - last] is not None:
                    A[i][j] = A[i - 1][j - last] + [last]
                else:
                    A[i][j] = None

    return A[-1][-1]


if __name__ == "__main__":
    s = [12, 1, 61, 5, 9, 2]
    add_list = []
    result = FindAddList().find_add_list(s, 3, add_list)
    if result:
        print(add_list)
