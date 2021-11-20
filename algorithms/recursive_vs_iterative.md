# recursive function

하나의 함수에서 자신을 다시호출하여 작업을 수행
recursively

### binary trees 
-> 왼쪽 서브트리의 원소들은 모두 작거나 같을 것, 오른쪽 서브트리의 원소들은 모두 클 것 
-> 이 원칙을 모든 노드에 대해서 적용
- tree search  

### 간단한 예 
- 자연수의 합 구하기
sigma 이용처럼, 1부터 n까지 모든 자연수의 합 
Recursive version
```
def sum(n):
    # print(n)
    if n <= 1:
        return n
    else:
        return n + sum(n-1)

a = int(input("Number: "))
print(sum(a))
```

- 재귀 호출의 종결조건이 매우 중요
알고리즘의 종결조건에 반드시 필요.
-> 인자로 주어진 n이 만족할 경우 어떻게하고, 아닐경우 어떻게 한다.


- 모든 재귀 알고리즘은 그와 대칭되는 반복되는 알고리즘이 있다. while 순환문- 반복적(iterative version)
```
def sum(n):
    s = 0
    while n>= 0:
        s += n
        n -= 1
    return s

a = int(input("Number: "))
print(sum(a))
```

복잡도는 O(n)
효율도 -> iterative가 높다.
효율적인 측면에선 recursive 조심해야함...

recursive version은 사실 아래 함수로도 표현 가능 이건 시간복잡도 O(1)임. 효율성 측면에서는 좋은데, 이걸 알고리즘이라고 할 수 있을까?
```
def sum(n):
    return n*(n+1) //2
```

factorial 함수 
```
def factorial(n):
    if n<= 1:
        return 1
    else:
        return n*factorial(n-1)
```

