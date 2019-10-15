class spam:
    def __init__(self,string):
        self.string=string

    def show(self):
        return self.__dict__
    


@spam
class spam2:

    def __init__(self,data):
        self.number=data

    def show(self):
        return self.__dict__

    def re_call_init(self):
        super.__init__(spam2)
