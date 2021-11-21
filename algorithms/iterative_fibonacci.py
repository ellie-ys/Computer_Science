#python unpacking, packing 사용
def fibonacci(n):
    s = 1
    if n < 2:
        return n
    a,b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b


n = int(input())

for n in range(1, n+1):
    print(n, fibonacci(n))


#refer : https://www.python.org/ 피보나치 함수