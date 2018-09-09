from random import randrange


def make_card_list():
    return [i for i in range(52)]


def shuffle_the_list(input_list):
    if not input_list:
        return

    length = len(input_list)
    for i in range(length):
        random_target = randrange(i, length)
        input_list[i], input_list[random_target] = input_list[random_target], input_list[i]


if __name__ == "__main__":
    card_list = make_card_list()
    print(card_list)

    shuffle_the_list(card_list)
    print("after shuffle {}".format(card_list))
