def digit_match(n, m):
    if n < 10:
        return int(n == m % 10)
    if m < 10:
        return int(m == n % 10)

    return int(n % 10 == m % 10) + digit_match(n // 10, m // 10)


def main():
    print('Enter n:')
    n = int(input())
    print('Enter m:')
    m = int(input())
    print('{} and {} share {} common digits!'.format(n, m,
                                                     digit_match(n, m)))


if __name__ == '__main__':
    main()
