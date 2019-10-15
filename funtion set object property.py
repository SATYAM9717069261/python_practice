class trace:
    def __init__(self,nam):
        self.name=nam

    def __call__(self):      
        return self.__dict__,self.name()   # call spam() method



@trace               # that means spam=trace(spam())
def spam():
    return "hii"

