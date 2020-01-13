import ast


def second_best_recursive(lst):
    pass


def main():
    print('Please enter a list of numbers of size >= 2:')
    lst = ast.literal_eval(input())
    print('The second largest number in the list is {}'.format(second_best_recursive(lst)))


if __name__ == '__main__':
    main()
