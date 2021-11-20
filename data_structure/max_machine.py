# 최댓값 기계
# 이번 실습에선 다양한 메서드를 가진 클래스를 만들어보겠습니다.

# 이 클래스는 자신만의 배열을 가지고 있고, 그 배열에 숫자를 추가하는 메서드와 배열에 정수를 제거하는 메서드와 배열에서 제일 큰 정수를 찾는 메서드로 구성되어있습니다.

# machine.addNumber(x) : 정수 x를 최댓값 기계 machine에 추가합니다.
# machine.removeNumber(x) : 정수 x를 최댓값 기계 machine으로부터 제거합니다. 만약 정수 x가 최댓값 기계 내에 없다면 아무 일도 일어나지 않습니다.
# machine.getMax() : 최댓값 기계 machine이 갖고있는 숫자들 중 최댓값을 반환합니다.


class maxMachine :
    def __init__(self) :
    # 객체 생성될 때 자동으로 호출되는 함수!
    #__$$$$__: magic method - 파이썬 내부 라이브러리에서 좀 특수하게 작동    
        self.numbers = []
        
    def addNumber(self, n) :
        self.numbers.append(n)

    def removeNumber(self, n) :
        self.numbers.remove(n)

    def getMax(self) :
        return max(self.numbers)


def main():

    myMachine = maxMachine()

    n = int(input())
    
    for _ in range(n) :
        line = [int(v) for v in input().split()]
        if line[0] == 0 :
            myMachine.addNumber(line[1])
        elif line[0] == 1 :
            myMachine.removeNumber(line[1])
        elif line[0] == 2 :
            print(myMachine.getMax())

    
if __name__ == "__main__":
    main()



# 지시 사항
# 입력
# 첫 번째 줄에 최댓값 기계가 수행할 명령의 수를 나타내는 정수 nnn을 입력합니다. ( 500≤n≤55000500 \le n \le 55000500≤n≤55000)

# 두 번째 줄부터 n개의 줄에 걸쳐 수행할 명령을 입력합니다. 명령의 종류는 다음과 같습니다.

# 0 x : 정수 x를 입력
# 1 x : 정수 x를 제거
# 2 : 최댓값 반환
# 입력 예시
# 9
# 0 1
# 0 2
# 0 4
# 0 5
# 2
# 1 5
# 2
# 1 2
# 2

# 출력 예시
# 5
# 4
# 4