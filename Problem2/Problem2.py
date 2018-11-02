class Data:
    def __init__(self):
        self.data = []
        self.size = 0
    
    def add(self, val):
        self.data.append(val)
        self.size += 1
        
        
    def remove(self):
        temp = self.data[self.size-1]
        self.size -=1
        array = []
        for i in range(0, self.size):
            array.append(self.data[i])
        self.data = array
        print(temp)
        return temp
        
        
    def getValue(self, index):
        if index > self.size-1:
            return -1
        else:
            return self.data[index]
            
    
    
        
d = Data()
d.add(1)
d.add(9)
d.add(4)
d.add(5)
d.add(10)
d.add(0)
print(d.getValue(0))
print(d.getValue(3))
