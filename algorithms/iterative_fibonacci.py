def fibonacci(n):
    s = 1
    while n >= 2:
        s = (n-1) + (n-2)
        n -= 1

    return s


n = int(input())

print(fibonacci(n))


# 삼항 연산자 사용
# def fibo(n):
#     return fibo(n-1) + fibo(n-2) if n>=2 else n


# for n in range(1, 11):
#     print(n, fibo(n))