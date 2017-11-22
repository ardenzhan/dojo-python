# Foo and Bar
# print all prime (foo) numbers and all perfect squares (bar)
# between 100 and 100,000

min = 100
max = 150
notPrime = []
for x in range(2, max+1):
    z = 1
    while z*z <= x:
        if z*z == x:
            print x, "bar"
        z = z + 1

    if x not in notPrime:
        print x, "foo"
        for y in range(x*x, max+1, x):
            notPrime.append(y)
    else:
        print x, "foobar"

#Sieve of Eratosthenes for primes
