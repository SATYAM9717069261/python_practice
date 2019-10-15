class personal_data:

    def __get_age__(self):
        return self.__age__
    def set_age(self,ag):
        self.__age__=ag   # here use UnderScope foor set attribute
        return "Set you age"
    age=property(__get_age__,set_age,None,None)  # first Arg of Property required 1 argument and 2 one required 2 Argument

# property(funtion1,funtioon2) funtion1 have 1 argument , function2 have 2 argument


