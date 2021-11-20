'''
내림차순 정렬하기 이전 maxMachine class 가져와서 sorting등 두 개의 클래스 만들기
'''
class maxMachine :

    def __init__(self) :
        self.numbers = []

    def addNumber(self, n) :
        self.numbers.append(n)

    def removeNumber(self, n) :
        self.numbers.remove(n)

    def getMax(self) :
        return max(self.numbers)

def sorting(myList) :

    myMachine = maxMachine()

    result = []
    for element in myList:
        myMachine.addNumber(element)
    for _ in range(len(myList)):
        myMax = myMachine.getMax()

        result.append(myMax)
        myMachine.removeNumber(myMax)
    return result

def main():

    myList = [int(v) for v in input().split()]

    print(sorting(myList))

if __name__ == "__main__":
    main()



'''
숫자들이 주어질 때, 이를 내림차순 정렬하여 출력하는 프로그램을 작성하세요.

단, ‘최댓값 기계’문제에서 작성하였던 자료구조를 이용하여 문제를 풀도록 합니다.

숫자들을 최댓값 기계에 넣고, 최댓값 기계에서 반환되는 숫자들을 받아 출력하면 됩니다.


지시사항
입력
첫째줄에 nnn개의 정수들이 공백으로 구분되어 입력됩니다. (100≤n≤200000100 \le n \le 200000100≤n≤200000)

출력
입력된 정수들을 내림차순으로 정렬하여 출력합니다.

입력 예시
2 5 1 4 4 3 2
Copy
출력 예시
5 4 4 3 2 2 1
'''