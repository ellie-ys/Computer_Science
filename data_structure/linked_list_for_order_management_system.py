'''
주문관리시스팀, 이중 연결리스트
'''

class LinkedListElement :
    def __init__(self, data, myPrev, myNext) :
        self.data = data
        self.myPrev = myPrev
        self.myNext = myNext
        
class orderManager :
    def __init__(self) :
        self.start = None
        self.end = None

    def addOrder(self, orderId) :
        o = LinkedListElement(orderId, None, None) 
        
        if self.start == None and self.end == None :
            self.start = o
            self.end = o

        else :
            self.end.myNext = o
            o.myPrev = self.end

            self.end = o

    def removeOrder(self, orderId) :
        if self.start == None and self.end ==None :
            #링크드리스트에 아무것도 없는 경우
            return 

        #현재 가지고 있는 노드
        current = self.start
 

        while current != None:
            if current.data == orderId :
                prevElem = current.myPrev#임시로 들고있는다.
                nextElem = current.myNext

                if prevElem != None : #이전데이터가 none이 아니다
                    prevElem.myNext = nextElem 
                #[prevElem]<->[current]<->[nextelem]
                if nextElem != None :
                    nextElem.myPrev = prevElem

                if current == self.end : #현재의 노드가 end라면,
                    self.end = prevElem

                if current == self.start:
                    self.start = nextElem

            current = current.myNext
            #while문이 계속 돌면서 current값이 변하게 된다.


    def getOrder(self, orderId) :
        cnt = 0
        if self.start == None and self.end == None:
            return -1
        current = self.start

        while current != None:
            if current.data == orderId :
                return cnt + 1
            
            current = current.myNext
            cnt = cnt + 1

        #연결리스트에   orderid값이 없다, 
        return -1

def main():

    line = [int(v) for v in input().split()]
    m = line[0]
    
    manager = orderManager()

    for _ in range(m) :
        line = [int(v) for v in input().split()]

        if line[0] == 1 :
            manager.addOrder(line[1])

        elif line[0] == 2 :
            manager.removeOrder(line[1])

        elif line[0] == 3 :
            myOrder = manager.getOrder(line[1])

            if myOrder == -1 :
                print("-1")
            else :
                print(str(manager.getOrder(line[1])))

if __name__ == "__main__":
    main()


'''
이번 실습문제에서는 orderManager class내의 함수 addOrder, removerOrder, getOrder를 통해 위 기능을 구현합니다.

addOrder(x) : 주문번호 x를 주문 관리 시스템에 추가합니다. return 값은 없습니다.
removeOrder(x) : 주문번호 x를 주문 관리 시스템에서 제거합니다. 입력되는 x 값은 항상 주문 관리 시스템에 존재함이 보장됩니다. return 값은 없습니다.
getOrder(x) : 입력한 주문번호 x가 주문 관리 시스템에서 몇 번째로 처리되는지를 return 합니다. 만약 입력한 주문번호 x가 주문 관리 시스템 내에 존재하지 않는 경우 -1을 return 합니다.
예를 들어, addOrder(1), addOrder(2), addOrder(4)를 차례로 실행하면 주문 관리 시스템에 1 - 2 - 4로 입력된 순서대로 저장됩니다. 이 상태에서 removeOrder(2)를 실행하면 주문 관리 시스템에서 주문번호 2를 찾아낸 다음 제거하여 1 - 4 로 주문 관리 시스템이 업데이트됩니다.

이 상황에서 getOrder(1)를 실행한 결과는 주문번호 1이 처리될 순서인 1이 반환되며, getOrder(4)를 실행한 결과는 주문번호 4가 처리될 순서인 2가 반환될 것입니다.

요구사항
연결 리스트를 이용하여 구현해주시기 바랍니다.


지시사항
이번 문제는 테스트 케이스가 총 20개입니다. 테스트 케이스 1번부터 10번까지는 작성하신 주문관리 시스템이 제대로 동작하는지를 체크하며, 11번부터 20번까지는 작성하신 주문관리 시스템의 성능을 잽니다.

11번부터 15번까지는 주문 조회를 매우 많이 할 경우, 16번부터 20번까지는 주문 조회를 거의 하지 않을 경우입니다. 이 두 경우에 대하여 리스트를 활용한 구현과 링크드 리스트를 활용한 구현의 성능 차이를 보도록 합니다.

입력
첫째 줄에 주문관리 시스템이 처리할 명령의 개수를 의미하는 정수 n이 입력됩니다.

둘째 줄부터 n개의 줄에 걸쳐서 명령의 정보가 주어집니다.

명령은 공백으로 구분된 2개의 정수로 입력되며, 3가지 종류가 있습니다.

1 x의 경우 주문번호 x를 추가
2 x의 경우 주문번호 x를 삭제
3 x의 경우 주문번호 x를 조회
입력 예시 1
10
1 1
1 2
1 4
2 2
3 1
3 4
1 2
2 1
1 1
3 2
Copy
출력 예시 1
1
2
2
Copy
입력 예시 2
10
1 4
1 8
3 8
1 2
1 1
2 4
3 8
1 59
1 5959
3 59
Copy
출력 예시 2
2
1
4
Copy
입력 예시 3
11
1 2
2 2
1 1818
1 8282
1 2255
1 6515
2 1818
1 486
3 486
3 3
1 4860
Copy
출력 예시 3
4
-1

'''