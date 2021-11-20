'''
배열로 구슬넣는 파이프를 구현해보기 -  배열
이 파이프를 갖는 ADT(추상적 자료형)은 구현방법을 지정하는 게 아니라서 어떻게 구현하는지는 상관이 없다.
그래서, 배열과 연결리스트로 구현해보기로 함.

아래에서 배열을 이용한 파이프 구현에서
최악의 경우 시간복잡도(Big O)가 n^2으로 나옴.

효율적인 목적 달성을 위해 특성에 맞는 자료구조를 설계하고 사용해야 한다.
'''


class ListPipe:

    def __init__(self) :
        self.myPipe = []
        

    def addLeft(self, n) :
        self.myPipe.insert(0,n) #0번째 위치에 n이라는 것을 넣어주게 된다.
        

    def addRight(self, n) :
        self.myPipe.append(n)

    def getBeads(self) :
        return self.myPipe
        

def processBeads(myInput) :

    myPipe = ListPipe()
    for bead, direction in myInput:
        # 구슬번호와 방향, 넣어준 대로 출력
        # print(bead, direction)
        if direction == 0 :
            #왼쪽
            myPipe.addLeft(bead)
        elif direction == 1:
            #오른쪽
            myPipe.addRight(bead)
        else:
            pass


    result = myPipe.getBeads()
    #구슬의 배치가 result

    return result


def main():
    n = int(input())
    myList = []

    for _ in range(n) :
        myList.append([int(v) for v in input().split()])

    print(*processBeads(myList))

if __name__ == "__main__":
    main()

'''
문제
구슬 넣기 (배열)
Elice의 토끼는 암기력을 높이기 위해 구슬 넣기 놀이를 고안했습니다.

토끼는 nnn개의 구슬이 있으며, 각 구슬은 1부터 nnn까지의 번호를 하나씩 갖고 있습니다. 또한, 토끼는 양 쪽이 뚫려있고 투명하지 않은 관을 갖고 있습니다.

토끼는 nnn개의 구슬을 이 파이프에 무작위로 넣은 후에, 최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 암기함으로써 암기력을 높이려고 합니다.

토끼는 파이프의 왼쪽에, 혹은 오른쪽에 구슬을 넣을 수 있습니다. 예를 들어, 파이프의 왼쪽으로 숫자 1의 구슬을 넣고, 파이프의 오른쪽으로 숫자 3의 구슬을 넣고, 마지막으로 파이프의 왼쪽으로 숫자 2의 구슬을 넣게 되면, 최종적으로 구슬의 배치는 2 1 3 이 됩니다.

토끼가 nnn개의 구슬을 파이프에 넣는 행위가 입력으로 주어질 때, 최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력하는 프로그램을 작성하세요.

(단, 파이프의 길이는 nnn개의 구슬을 모두 담기에 충분히 길다고 가정합니다.)

지시사항
입력
입력의 첫 번째 줄에는 구슬의 개수 nnn이 주어집니다. (100≤n≤200000100 \le n \le 200000100≤n≤200000)

두 번째 줄부터는 토끼가 구슬을 넣는 행위가 주어집니다.

각 줄은 두 개의 정수 aaa, bbb로 이루어지며, 이 뜻은 구슬 aaa를 왼쪽 혹은 오른쪽으로 넣는다는 의미입니다. (1≤a≤10000000001 \le a \le 10000000001≤a≤1000000000)

(bbb가 0이면 왼쪽, bbb가 1이면 오른쪽이며 그 외의 입력은 주어지지 않는다)

출력
최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력한다.


입력 예시
3
1 0
2 1
3 0

출력 예시
3 1 2
'''