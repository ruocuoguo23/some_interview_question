

def cal_string_distance(str1, str2):
    if not str1 or not str2:
        return max(len(str1), len(str2))

    dis1 = 1 + cal_string_distance(str1[1:], str2)
    dis2 = 1 + cal_string_distance(str1, str2[1:])
    dis3 = cal_string_distance(str1[1:], str2[1:]) if str1[0] == str2[0] else 1 + cal_string_distance(str1[1:],
                                                                                                      str2[1:])

    return min(dis1, dis2, dis3)


if __name__ == "__main__":
    test_string1 = "kitten"
    test_string2 = "sitting"
    print(cal_string_distance(test_string1, test_string2))
