while True:
    try:
        dan = int(input("단을 입력하시오: "))
        break
    except ValueError:
        print("숫자를 입력하시오.")

def gugudan(dan):
    for i in range(1, 10):
        print('{} * {} = {}'.format(dan, i, dan * i))

def main():
    gugudan(dan)

if __name__ == "__main__":
    main()



