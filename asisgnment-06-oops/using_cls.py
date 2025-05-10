

class counter:
    
    count = 0 

    def __init__(self):
        counter.count += 1

    def display__count(cls):
        print("Total Object Count:", cls.count)



c1 = counter()
c2 = counter()
c3 = counter()

# Display total objects created
c1.display__count()
c2.display__count()
c3.display__count()