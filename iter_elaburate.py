class it:
    def __init__(self,value):
        self.data=value

    def __getitem__(self,i):
        print("Get => ")
        return self.data[i]

    def __iter__(self):
        print("Iter => ")
        self.ix=0
        return self

    def __next__(self):
        print("Next => ")
        if self.ix==len(self.data):
            raise StopIteration
        item=self.data[self.ix]
        self.ix+=1
        return item

    def __contains__(self,x):
        print("Contains => ")
        return x in self.data

    next=__next__


if __name__=='__main__':
    X=it([1,2,3,4,5,6,7,8,9,0])
    print(3 in X)
    for i in X:
        print(i,end='|')
    print("--------------------------------------")
    print([i for i in X])
    print(list(map(bin,X)))
    I=iter(X)
    while True:
        try:
            print(next(I),end="<-->")
        except StopIteration:
            break
