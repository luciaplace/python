''' while문
    while 반복조건 :
        반복할 문장 '''

#1
iloop = 0
while iloop <5:
    print("Programming")
    iloop += 1

#2
sum = 0
val = 0
while val <11:
    sum += val
    val += 1
print('1에서 10까지의 합', sum)

#3
sum =0
val = 1
while val <100:
    sum += val
    val += 2
print('1부터 100까지의 홀수의 합', sum )

#4 구구단

val = 1
dan = int(input("단 수를 입력하시오 :"))
while val < 10:
    print(dan,'*',val,'=',dan*val)
    val+=1

#5 구구단

dan = 2
while dan <10:
    val =1
    while val <10:
        print("%d * %d = %d" %(dan, val, dan*val))
        val += 1
    dan+=1
    print()
