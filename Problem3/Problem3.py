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
            
            
def ProblemThree(data, value):
    i = 1 
    compare = 0
    count = 1
    while count == 1:
        if value == data.getValue(i):
            compare +=1
            print("compares:" + str(compare))
            return value
        elif value > data.getValue(i):
            compare+=1
            i*=2
        elif value < data.getValue(i):
            compare+=1
            i-=1
        else:
            print("value not Found!")
    
            
d = Data()
d.add(1)
d.add(5)
d.add(8)
d.add(10)
d.add(12)
d.add(14)
d.add(18)
d.add(20)
d.add(33)
d.add(41)
print(ProblemThree(d, 8))
print(ProblemThree(d, 33))

        
        