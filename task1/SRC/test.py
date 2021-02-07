import sys


def my_func(*args):
    print('begin')
    if len(args) == 3:
        print(1)
    elif len(args) == 4:
        print(2)
    print('end')


def main():
    my_func(sys.argv)


if __name__ == "__main__":
    main()
