def is_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_number_spa(n):
    spa = []
    cnt = 0
    for i in range(2, n + 1):
        if is_prime_number(i):
            spa.append(i)
            cnt += 1
    return print("{}까지의 정수 중 소수는 {}로, 총 {}개이다.".format(n, spa, cnt))

# x부터 y까지의 prime number와 총 개수 구하기.
def prime_number_t100(x, y):
    spa = []
    cnt = 0
    for i in range(x, y + 1):
        if is_prime_number(i):
            spa.append(i)
            cnt += 1
    return print("{}부터 {}까지의 정수 중 소수는 {}로, 총 {}개이다.".format(x, y, spa, cnt))

prime_number_t100(100, 200)
