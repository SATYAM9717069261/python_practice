                                    # print  secand Highest value
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sht_lis=[]
    for j in range(n):
        arry=arr
        ma_x=arry[0]
        for i in arry:
            if ma_x<i:
                ma_x=i
        sht_lis.append(ma_x)
        arr.remove(ma_x)
    l=1
    for j in sht_lis:
        for i in sht_lis[l:]:
            if j==i:
                sht_lis.remove(j)
        l+=1
    print(sht_lis[1])
    
    
