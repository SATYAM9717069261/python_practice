class test:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
        self.lis=[]
        
    def add(self):
        self.sum=self.num1+self.num2
        #print(self.lis)
        return self.sum
    
    def __getitem__(self,index):
        if self.lis:       # that can use for if list Already Write then it can't Re-Write
            pass
        else:
            for i in dir(self):
                if i.startswith('_'):
                    pass
                else:
                    self.mak_li(i)
        return self.lis[index]        
    
    def __setitem__(self,index,data):
        if self.lis:
            self.mak_li(data,index)
        else:
            eval('self[:]')    # Can't use Equal sign in eval
            self.__setitem__(index,data)
        return self.lis            

    def mak_li(self,k,index=None):
        # mak_li(object, data,index=None)  index for insert Data in Specify Place 
        if index:
            self.lis.insert(index,k)       
        else:
            self.lis.append(k)
            
        
