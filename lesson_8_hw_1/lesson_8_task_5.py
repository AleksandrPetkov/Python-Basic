"""
Function 'gen_primes' output all prime numbers from 1 to 100.
"""


def gen_primes():
    numbers = []
    for i in range(1, 100):
        if i == 1:
            print('Number 1 isn\'t prime or compound number, it is just 1')
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            numbers.append(i)
    return numbers


def main():
    print('Prime numbers from 1 to 100 are: ', gen_primes())


main()
