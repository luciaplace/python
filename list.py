''' List :
    리스트 명 = [값1,값2,값3 .....]'''

#1
li = [i for i in range(1,11)]
sum = 0
for i in range(0,10):
    sum += li[i]
print(sum)

''' list.append(value):
        리스트에 값 추가하기 '''

#2
sum =0
ktx =[]
ktx.append(1)
ktx.append(2)
ktx.append(3)
ktx.append(4)
ktx.append(5)

for i in range(0,5):
    sum += ktx[i]
print(sum)


#3
sum =0
ktx=[]
for i in range(0,5):
    ktx.append(i+1)

for i in range(0,5):
    sum += ktx[i]
print(sum)
