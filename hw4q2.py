def digit_match(n, m):
    pass


def main():
    print('Enter n:')
    n = int(input())
    print('Enter m:')
    m = int(input())
    print('{} and {} share {} common digits!'.format(n, m, digit_match(n, m)))


if __name__ == '__main__':
    main()
