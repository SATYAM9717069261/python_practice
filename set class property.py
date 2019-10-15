class trace:
    def __init__(self,nam):
        self.name=nam

    def __call__(self):
        self.__dict__



@trace
def spam():
    return "hii"

