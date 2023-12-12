from random import randint

import argparse


def sort_by_insertion(arr):
    _arr = arr[:]
    _length = len(_arr)
    for i in range(0, _length - 1):
        i += 1
        key = _arr[i]
        for j in range(i):
            if _arr[j] >= key:
                _arr[j+1: i+1] = _arr[j: i] 
                _arr[j] = key
                break
    return _arr

def generate_rnd_arr(length, rand_range):
    _arr = []
    for i in range(length):
        _arr.append(randint(-1 * 2**rand_range, 2**rand_range))

    return _arr


def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Please add array length and power for random numbers. Defaults are both 10")
    parser.add_argument('length', metavar='L', type=positive_int, default=10, nargs='?', help='Array length')
    parser.add_argument('power', metavar='P', type=positive_int, default=10, nargs='?', help='Power for random numbers')
    args = parser.parse_args()

    rand_arr = generate_rnd_arr(args.length, args.power)
    sorted_rand_arr = sort_by_insertion(rand_arr)
    print(rand_arr)
    print(sorted_rand_arr)
    print()
