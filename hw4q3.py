import ast


def second_best_recursive(lst):
    first_value = lst[0]
    second_value = lst[1]
    if len(lst) == 2:
        return min(first_value, second_value)

    third_value = lst[2]
    min_value = min(first_value, second_value, third_value)

    if min_value == first_value:
        del lst[0]

    elif min_value == second_value:
        del lst[1]
    else:
        del lst[2]

    return second_best_recursive(lst)


def main():
    print('Please enter a list of numbers of size >= 2:')
    lst = ast.literal_eval(input())
    print('The second largest number in the list is {}'.format(
        second_best_recursive(lst)))


if __name__ == '__main__':
    main()
