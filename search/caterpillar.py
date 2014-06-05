# coding=utf-8
"""
@see: https://codility.com/media/train/13-CaterpillarMethod.pdf

Let’s check whether a sequence a[0], a[1], ... , a[n−1] (1 < a[i] < 10^9)
contains a contiguous subsequence whose sum of elements equals s.
"""


def _print_subsequences(a, back, front):
    first_row = '|'.join([str(ai).rjust(5) for ai in a])
    second_row = '-' * len(first_row)
    third_row = '|'.join([('back' if i == back else '' +
                          'front' if i + 1 == front else '').rjust(5)
                          for i in range(0, len(a))])

    return '\n'.join([first_row, second_row, third_row]) + '\n'


def subsequences(a, s, verbose=True):
    """
    At the ﬁrst glance we have two
    nested loops, what suggest quadratic time. However, notice that at every step we move the
    front or the back of the caterpillar, and their positions will never exceed n. Thus we actually
    get an O(n) solution.
    """
    solutions = []
    n = len(a)
    front, total = 0, 0
    for back in xrange(n):
        while front < n and total + a[front] <= s:
            total += a[front]
            front += 1

        if total == s:
            solutions.append(a[back:front])
            if verbose:
                print _print_subsequences(a, back, front)
        total -= a[back]
    return solutions


print subsequences([1, 2, 3, 4, 5, 6, 7, 8], 6)


"""
Problem: You are given n sticks (of lengths 1 <= a[0] <= a[1] <=...<= a[n−1] <= 10^9). The goal is
to count the number of triangles that can be constructed using these sticks. More precisely,
we have to count the number of triplets at indices x < y < z, such that a[x] + a[y] > a[z].
"""


def _print_triangles(a, x, y, z):
    first_row = '|'.join([str(ai).rjust(5) for ai in a])
    second_row = '-' * len(first_row)
    third_row = '|'.join([('x' if i == x else '' +
                          'y' if i == y else '' +
                          'z' if i == z else '').rjust(5)
                          for i in range(0, len(a))])

    return '\n'.join([first_row, second_row, third_row]) + '\n'


def triangles(a, verbose=True):
    """
    The time complexity of the above algorithm is O(n^2),
    because for every stick x the values of
    y and z increase O(n) number of times.
    """
    n = len(a)
    result = 0

    for x in xrange(n):
        z = 0
        for y in xrange(x + 1, n):
            while z < n and a[x] + a[y] > a[z]:
                z += 1

            result += z - y - 1

            if verbose:
                print _print_triangles(a, x, y, z)

    return result


print triangles([1, 2, 3, 4, 5, 6, 7, 8])