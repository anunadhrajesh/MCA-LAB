def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1
print (is_coprime(17, 13))
print (is_coprime(5, 7))
print (is_coprime(10, 20))