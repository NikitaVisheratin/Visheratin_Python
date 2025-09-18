def extended_gcd(first, second):
    if first == 0 and second == 0:
        return 0, 0, 0
    
    A = abs(first)
    B = abs(second)
    x0, y0 = 1, 0
    x1, y1 = 0, 1

    while B != 0:
        q = A // B
        A, B = B, A - q * B
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    if first < 0: x0 = -x0
    if second < 0: y0 = -y0
    return A, x0, y0

if __name__ == "__main__":
    int_1, int_2 = map(int, input().split())
    g, a, b = extended_gcd(int_1, int_2)
    print(f'{g} = {a} * {int_1} + {b} * {int_2}')
