import sys


def i_to_base(nb, base_src=10, base_dst="0123456789"):
    #
    if isinstance(nb, str):
        n = int(nb, int(base_src))
    else:
        n = int(nb)
    #
    bd_len = len(base_dst)
    if n < bd_len:
        return base_dst[n]
    else:
        return i_to_base(n // bd_len, bd_len) + base_dst[n % bd_len]


def main():
    if len(sys.argv) == 3:
        res = i_to_base(sys.argv[1], base_dst=sys.argv[2])
    elif len(sys.argv) == 4:
        res = i_to_base(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        res = ("Usage: 1st argument - the number to be converted\n")
        res += ("       2nd argument - base")

    print(res)


if __name__ == "__main__":
    main()
