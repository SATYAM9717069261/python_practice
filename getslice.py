class exp:
    def __getslice__(self,a,b):
        return "Call get-slice"
    def __getitem__(self,a):
        return "Call Getitem"

    
