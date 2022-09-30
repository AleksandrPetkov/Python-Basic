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


def gen_primes_eratosfen(number):
    prime = [True for i in range(number+1)]
    prime_n = []
    p = 2
    while p * p <= number:
        if prime[p] is True:
            for i in range(p * p, number+1, p):
                prime[i] = False
        p += 1
    for p in range(2, number+1):
        if prime[p]:
            prime_n.append(p)
    return prime_n


if __name__ == '__main__':
    num = 100000
    print(f'Prime numbers from 1 to {num} are: ', gen_primes_eratosfen(num))
    print(f'Prime numbers from 1 to {num} using sieve of eratosthenes are: ', gen_primes_eratosfen(num))
