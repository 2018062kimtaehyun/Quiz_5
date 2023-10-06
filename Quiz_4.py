def print_gugudan_table(n):
    for i in range(1, n + 1):
        print(f"------[ {i} 단 ] ------")
        for j in range(1, 10):
            result = i * j
            print(f"{i} X {j} = {result}")

try:
    num = int(input("몇 단까지 출력할까요? "))

    if num < 1 or num > 19:
        print("1부터 19까지의 숫자를 입력하세요.")
    else:
        print_gugudan_table(num)
except ValueError:
    print("올바른 숫자를 입력하세요.")
