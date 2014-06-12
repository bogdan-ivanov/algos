
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


if __name__ == "__main__":
    demo_find()
