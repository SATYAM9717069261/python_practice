def exc(string,index):
    try:
        return string[index]

    except IndexError as a:
        return a

    else:
        print('That Call if Any error can\'t  raise')
        #raise()

    finally :
        print('Some Error Try Again')
    

try:
    exc(1,2,3)
except:
    print("Error")
