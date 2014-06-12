
"""
Rolling Hashes & Rabin-Karp
---------------------------

The Rabin-Karp string search algorithm is normally used with a very simple rolling hash function that only
uses multiplications and additions:

H = c_1 a^{k-1} + c_2 a^{k-2} + c_3 a^{k-3} + ... + c_k a^{0} where a is a constant and c_1, ..., c_k are the
input characters.

In order to avoid manipulating huge H values, all math is done modulo n. The choice of a and n is
critical to get good hashing; see linear congruential generator for more discussion.

Caveats:
--------
Hashing collisions are a problem.
One way to deal with them is to check for a match when two fingerprints are equal,
but this makes the solution inefficient if there are lots of matches.
Another way is to use more hashing functions to decrease the collision probability.
"""

import collections


def find(needle, haystack):
    """
    Find all occurances of needle in haystack
    """
    A = 10                  # The constant coefficient
    MOD = 29              # Prime number used for modulo

    m = len(haystack)
    n = len(needle)

    if m < n:               # precondition
        return []

    an = 1                  # Init a^n as a^0
    offsets = []            # results

    hash_haystack = 0       # init hashes
    hash_needle = 0

    for c in needle:
        hash_needle = (hash_needle * A + int(c)) % MOD

    print 'hash_needle=', hash_needle

    # an = 1

    for c in haystack[:n]:
        hash_haystack = (hash_haystack * A + int(c)) % MOD
        an = (an * A) % MOD

    print 'hash_haystack=', hash_haystack

    if hash_haystack == hash_needle:
        print "match, offset=", 0
        offsets.append(0)

    for i in range(1, m - n + 1):
        # Add to the rolling hash the number corresponding to the next char,
        # and subtract the number corresponding to the excluded char
        hash_haystack = (hash_haystack * A + int(haystack[i + n - 1]) - an * int(haystack[i - 1])) % MOD
        print 'hash_haystack=', hash_haystack
        if hash_haystack == hash_needle:
            print "match, offset=", i
            offsets.append(i)

    return offsets


def demo_find():
    needle = '313'
    haystack = '44411311166643134445553313'
    print find(needle, haystack)


def common_substring(str_a, str_b):
    """
    Longest common substring
    ------------------------
    Given two strings A and B, compute their longest common substring.
    Let's solve a simpler problem: Given two strings A and B, and a number X
    find if they have a common sequence of length X.
    We use the rolling hash technique to find the hash codes for all X length substrings of A and B.
    Then we check if there is any common hash code between the two sets,
    this means A and B share a sequence of length X.
    We then use binary search to find the largest X.
    The complexity of this algorithm is O(n log n).
    """
    A = 10                  # The constant coefficient
    MOD = 15485863             # Prime number used for modulo

    def _hashes_substrings(string, x):
        hashes = collections.defaultdict(list)

        # init hash
        hash = 0
        an = 1

        n = len(string)

        for c in string[:x]:
            hash = (hash * A + ord(c)) % MOD
            an = (an * A) % MOD
        hashes[hash].append(0)

        for i in range(1, n - x + 1):
            hash = (hash * A + ord(string[i + x - 1]) - an * ord(string[i - 1])) % MOD
            hashes[hash].append(i)

        return hashes

    len_a = len(str_a)
    len_b = len(str_b)

    # binary search for X
    left, right = 0, min(len_a, len_b) - 1
    X = -1
    while left < right:

        new_X = int(float(left + right) / 2)
        if new_X == X:
            break

        X = new_X
        if X == 0:
            break
        # print 'left=', left, 'right=', right, 'X=', X

        hashes_a = _hashes_substrings(str_a, X)
        hashes_b = _hashes_substrings(str_b, X)

        keys_a = hashes_a.keys()
        keys_b = hashes_b.keys()

        intersection = set(keys_a) & set(keys_b)

        # print intersection
        # print [hashes_a[i] for i in intersection]
        # print [hashes_b[i] for i in intersection]

        if intersection:
            left = X
        else:
            right = X

    if intersection:
        # print intersection
        example = list(intersection)[0]
        offset = hashes_a[example][0]
        return str_a[offset: offset + X], X

    return "", 0


def demo_substring():
    print common_substring('alabalaportocala', 'portocalamea')
    print common_substring('cccccc', 'bbbbbbbb')
    print common_substring('123456789', '987654321')
    print common_substring('a1b2c3d4e5f6', 'a1b2d5f6')
    print common_substring('11113333222211114444', '111445533322211114444')


if __name__ == "__main__":
    demo_find()
    demo_substring()

