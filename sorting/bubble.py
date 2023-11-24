from random import randint


def sort_by_bubble(arr):
    _arr = arr[:]
    _length = len(_arr)
    for i in range(_length):
        for j in range(1, _length):
            if _arr[j - 1] > _arr[j]:
                _arr[j - 1], _arr[j] = _arr[j], _arr[j - 1]
    return _arr

def generate_rnd_arr(length, rand_range):
    _arr = []
    for i in range(length):
        _arr.append(randint(-1 * 2**rand_range, 2**rand_range))

    return _arr


if __name__ == "__main__":
    rand_arr = generate_rnd_arr(10, 10)
    sorted_rand_arr = sort_by_bubble(rand_arr)
    print(rand_arr)
    print(sorted_rand_arr)
    print()
