class SimpleQueue:
    def __init__(self):
        self.data=[]
        self.count=0
    def getElementCount(self):
        return self.count
    def isQueueEmpty(self):
        return self.count==0
    #Adding element to front
    def enqueue(self,ele):
        self.data.append(ele)
        self.count+=1
        return self.count
    #To remove element from rear
    def dequeue(self):
        if not self.isQueueEmpty():
            self.count-=1
            return self.data.pop(0)
        else:
            return None
    #To get element at rear
    def peek(self):
        if not self.isQueueEmpty():
            return self.data[0]
        else:
            return None
    def printElements(self):
        return self.data
    