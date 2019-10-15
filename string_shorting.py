name=input()
alp='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')

string=[i for i in name if i.isalpha()]
num=[i for i in name if i.isdigit()]

# Shorting Alphabats
re_name=''
#print(string)
min_str=string[0]

for i in range(len(string)):
    for i in string:
        if alp.index(min_str) > alp.index(i):
            min_str=i
            
    re_name+=min_str
    string.remove(min_str)
    if len(string)!=0:
        min_str=string[0]

# Shorting Numbers
re_num=''

if num:             # if name has no number then min_num =num[0] Generate Error
    min_num=num[0]
    for i in range(len(num)):
        for i in num:
            if int(min_num)> int(i):
                min_num=i
        re_num+=min_num
        num.remove(min_num)
        if len(num)!=0:
            min_num=num[0]
    re_num=list(re_num)

    # arrange Numbers
    ev=''
    ze=''
    odd=''
    for i in re_num:
        if int(i)%2 == 1:
            odd+=i
        #re_num.remove(i)

    for i in re_num:
        if int(i) == 0:
            ze+=i

    for i in re_num:
        if int(i)%2==0:
            if int(i)!= 0:
                ev+=i
    re_num=odd+ze+ev

name=re_name+re_num
print(name)
