def name_short(nam1,nam2):
	nam_1,nam_2=nam1.upper(),nam2.upper()

	if nam1==nam2:
		return nam1
	
	if len(nam_1)<len(nam_2):
		gap=len(nam_2)-len(nam_1)
		nam_1=nam_1+('Z'*gap)

	if len(nam_2)<len(nam_1):
		gap=len(nam_1)-len(nam_2)
		nam_2=nam_2+('Z'*gap)

	for (i,j) in zip(nam_1,nam_2):
		if alp.index(i)<alp.index(j):
			 return nam1
		if alp.index(i)>alp.index(j):
			 return nam2

if __name__ == '__main__':
    name=[]
    score=[]
    for i in range(int(input("Limit :"))):
        name.insert(i,input())
        score.insert(i,float(input()))

    alp='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')

    ma_x=score.index(max(score))

    max_index=[ j for (i,j) in zip(score,range(len(score))) if score[ma_x] == i ]

    name_max=[name[i] for i in max_index]

    nam_list=[]

    for i in name_max:
        nal=i
        for j in name_max:
            nal=name_short(nal,j)
        nam_list.append(nal)
        name_max.remove(nal)
    nam_list.append(name_max)

    nam_list=[a for a in nam_list if a ]
    print(nam_list)
    
            
    
