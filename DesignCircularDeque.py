class MyCircularDeque:

    def __init__(self, k: int):
        self.circularQueue=[None]*k
        self.front=0
        self.last=0
        self.size=k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.circularQueue[self.front-1]==None:
            self.circularQueue[self.front - 1]=value
            if self.front-1==-1:
                self.front=self.size-1
            else:
                self.front=self.front-1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.circularQueue[self.last]==None:
            self.circularQueue[self.last]=value
            if self.last+1==self.size:
                self.last=0
            else:
                self.last+=1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        temp=False
        if self.circularQueue[self.front]!=None:
            self.circularQueue[self.front]=None
            temp=True
            if self.front+1==self.size:
                self.front=0
            else:
                self.front+=1
        return temp

    def deleteLast(self) -> bool:
        temp=False
        if self.circularQueue[self.last-1]!=None:
            self.circularQueue[self.last-1]=None
            temp=True
            if self.last-1==-1:
                self.last=self.size-1
            else:
                self.last-=1
        return temp

    def getFront(self) -> int:
        if self.circularQueue[self.front]==None:
            return -1
        else:
            return self.circularQueue[self.front]

    def getRear(self) -> int:
        if self.circularQueue[self.last-1]==None:
            return -1
        else:
            return self.circularQueue[self.last-1]

    def isEmpty(self) -> bool:
        if self.circularQueue[self.front]==None:
            return True
        return False

    def isFull(self) -> bool:
        if self.circularQueue[self.front]!=None and self.front==self.last:
            return True
        return False
        
