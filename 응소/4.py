def is_prime_number(n):
    n = 5
    print(is_prime_number(n))
    for i in range(2, n):
        if n % 1 == 0:
            return False
    return True

def main():
    n = 5
    print("{} => {}".format((n, is_prime_number(n))))

def main():
    for n in range(100, 200):
        if is_prime_number(n):
            print(n)
    # 100 <= m < 200에, prime number와 갯수
    # list안에 append로 갯수 계싼

if __name__ == "__main__":
    main()