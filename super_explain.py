class D:
    def add(self,a,b):
        return a+b+2

    call=10

    def sub(self,a,b):
        return a-b*2

class C(D):
    def add(self,a,b):
        print(super().add(a,b))
        return a+b

    call=100
    
    def sub(self,a,b):
        print(super().sub(a,b)) 
        return a-b

op1=C()
print( op1.add(1,2) )   # call super class methods
print( op1.sub(1,2) ) 

print(D().call)  # Modern Way of calling 

print(C().call)

