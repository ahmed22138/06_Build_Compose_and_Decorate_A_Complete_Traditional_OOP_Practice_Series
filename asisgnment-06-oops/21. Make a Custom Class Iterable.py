

class Countdown:
    def __init__(self, start):  
        self.start = start
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value
        

count1 = Countdown(5)
for num in count1:
    print(num)
