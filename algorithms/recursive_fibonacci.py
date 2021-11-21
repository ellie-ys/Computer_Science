

def fibonacci(n):

    if n ==0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n = int(input())

print(fibonacci(n))


# 삼항 연산자 사용
# def fibo(n):
#     return fibo(n-1) + fibo(n-2) if n>=2 else n


# for n in range(1, 11):
#     print(n, fibo(n))