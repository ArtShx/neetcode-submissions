class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.c = capacity
        self.len = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        #print("pushback", self.arr, self.len, self.c)
        if self.len >= self.c:
            self.resize()
        
        self.arr[self.len] = n
        self.len += 1
        #print("pushback2", self.arr, self.len, self.c)

    def popback(self) -> int:
        #print("popback", self.arr, self.len)
        self.len -= 1
        out = self.arr[self.len]
        return out
        #return self.arr.pop()

    def resize(self) -> None:
        newc = self.c * 2
        self.arr = self.arr + [0] * self.c
        self.c = newc

    def getSize(self) -> int:
        return self.len
    
    def getCapacity(self) -> int:
        return self.c
