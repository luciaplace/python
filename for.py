''' for문
    for 변수 in range(시작값, 끝값, 증가값)'''

#1

sum = 0
for i in range(11):
    sum += i

print('1에서 10까지의 누적합:',sum)

#2

sum =0
for i in range(0,101,2):
    sum += i
print("1에서 100까지의 짝수합:", sum)

#3
favorite = int(input("내가 가장 좋아하는 숫자를 입력하시오."))
start = int(input('시작 :'))
end = int(input('끝 :'))

for i in range(start, end,1):
    if(favorite == i):
        print ("내가 좋아하는 숫자가 있습니다.")

#4 구구단

for val in range(1,10,1):
    print("2 * %d = %d" %(val, val*2))


#5 구구단

dan = int(input("단수를 입력하세요:"))
for val in range(1,10,1):
    print("%d * %d = %d" %(dan, val, val*dan))
