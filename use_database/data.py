class employ:
    def __init__(self,nam,sal):
        self.name=nam
        self.sallary=sal
    def out_info(self):
        return('Name = {}  Sallary =  {}'.format(self.name,self.sallary))
    def salry_updt(self,update):
        par=self.sallary*update/100
        self.sallary += int(par)
        

