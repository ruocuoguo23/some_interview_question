"""

"""


class CountTheDecodeNumber(object):

    @staticmethod
    def count_the_number(encoded_message):
        """

        :param encoded_message:
        :return:
        """
        if '0' in encoded_message:
            return 0

        if len(encoded_message) <= 1:
            return 1

        count_of_single_step = CountTheDecodeNumber.count_the_number(encoded_message[1:])
        count_of_double_step = 0 if test_message[:2] > '26' else CountTheDecodeNumber.count_the_number(
            encoded_message[2:])

        return count_of_single_step + count_of_double_step


if __name__ == "__main__":
    test_message = '111'
    print(CountTheDecodeNumber.count_the_number(test_message))
