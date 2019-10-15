class abc:
    def display(self,a):
        self.a=a
        print(self.a)


if __name__=='__main__':
#   Bounded Method Technic
    obj=abc()
    x=obj.display
    x(10)


#   Unbounded Method

    obj2=abc()
    x=abc.display
    x(obj2,10202)

#   Another Way Call Class Method

    abc().display(12)



