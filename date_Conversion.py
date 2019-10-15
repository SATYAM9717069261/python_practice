def timeConversion(s):
    a=s.split(':')
    result=''
 # For PM   
    if a[-1][2:]=='PM':
        if a[0]!='12':
            a[0]='{}:'.format(int(a[0])+12)
        else:
            a[0]='{}:'.format(int(a[0]))
        a[-1]=':{}'.format(a[-1][:2])
        for k in a:
            result+=k
                        
  # for AM
    if a[-1][2:]=='AM':
        if a[0]=='12':
            a[0]='0{}:'.format(int(a[0])-12)
        else:
            a[0]='0{}:'.format(int(a[0]))
        a[-1]=':{}'.format(a[-1][:2])
        for k in a:
            result+=k
        
    return result
