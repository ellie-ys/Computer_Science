'''개선된 Linked list
Dictionary, 해쉬 테이블 자료구조의 도움으로 '''


class LinkedListElement :
    def __init__(self, data, myPrev, myNext) :
        self.data = data
        self.myPrev = myPrev
        self.myNext = myNext

class orderManager :
    def __init__(self) :
        self.start = None
        self.end = None
        self.elems = {}

    def addOrder(self, orderId) :
        elem = LinkedListElement(orderId, None, None)
        #orderId는 key, elem은 value
        self.elems[orderId] = elem
        
        if self.start == None and self.end == None:
            self.start = elem
            self.end = elem
            
        else :
            self.end.myNext = elem
            elem.myPrev = self.end
            self.end = elem
        
    #dictionary 적극사용 하이라이트!
    def removeOrder(self, orderId) :
        if self.start ==None and self.end ==None:
            return
        #현재 정점 cur
        cur = self.elems[orderId]
        if self.start == cur and self.end == cur :
            self.start = None 
            self.end = None
        elif self.start == cur :
            self.start = cur.myNext
            cur.myNext.myPrev = None
            # [cur] -> [cur.myNext]  (왼쪽에 ->화살표 끊어주겠다는 의미)
        
        elif self.end == cur :
            self.end = cur.myPrev
            cur.myPrev.myNext = None
        else :
            cur.myPrev.myNext = cur.myNext
            cur.myNext.myPrev = cur.myPrev
            
        
    def getOrder(self, orderId) :
        cnt = 1
        cur = self.start
        
        while cur != None :
            if cur.data == orderId :
                return cnt
            cur = cur.myNext
            cnt = cnt + 1
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
