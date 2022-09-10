def all_even(x, y):
    total = 0
    for i in range(x, y + 1):
        if i % 2 == 0:
            total += i
    return total

print(all_even(1, 100))

#지능형 리스트 / 1-100까지 짝수의 합
all_even = [i for i in range(1, 101) if i % 2 == 0]
print(all_even)
print(sum(all_even))
