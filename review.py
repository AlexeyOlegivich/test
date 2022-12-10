from random import sample


def s(list_, target):
    left, right = 0, len(list_) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_[middle] < target:
            left = middle + 1
        elif list_[middle] > target:
            right = middle - 1
        else:
            return middle
    return


print(s([1, 2, 3, 4], 7))


if __name__ == "__main__":
    list_len = 10
    rand_list = sorted(sample(range(0, 101, 2), list_len))
    target = int(input('Pick a number between 0-100: '))
    target_index = s(rand_list, target)

    try:
        if 0 < target < 101:
            print(f'List: {rand_list}')
            if target_index is not None:
                print(f'Found {target} in index {target_index}')
            else:
                print(f'Cannot find {target} in the list')
        else:
            print('Число введено неверно')
    except ValueError:
        print('Invalid input')
