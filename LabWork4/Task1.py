import sys

def function(name):
    with open(name, 'r') as file:
        data = list(map(int, file.read().split()))

    ptr = 0
    n = data[ptr]
    ptr += 1
    k = data[ptr]
    ptr += 1
    a = data[ptr:ptr + n]

    min_left = [0] * n
    min_left[0] = a[0]
    for i in range(1, n):
        min_left[i] = min(min_left[i - 1], a[i])

    min_right = [0] * n
    min_right[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], a[i])

    min_product = float('inf')
    for j in range(k, n - k):
        left_min = min_left[j - k]
        right_min = min_right[j + k]
        product = left_min * a[j] * right_min
        if product < min_product:
            min_product = product

    mod = 10 ** 6 + 1
    print(min_product % mod)


if __name__ == "__main__":
    function("Test")
    function("27-167a.txt")
    function("27-167b.txt")