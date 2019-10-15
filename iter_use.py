class test:
    def __init__(self,start,lim):
        self.stat=start-1
        self.lim=lim
    def __iter__(self):
        print('a')
        return self
    def __next__(self):
        print('b')
        if self.stat==self.lim:
            raise StopIteration
        self.stat+=1
        return "{} next".format(self.stat)
