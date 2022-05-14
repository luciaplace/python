''' global : 전역변수
    함수 안에서 함수 밖의 전역변수를 사용할 때는 global + 변수명 으로 사용한다. '''

#1
hap = 100

def sum(value):
    hap = 20
    hap += value
    print('지역변수 hap 출력 :', hap)

sum(10)
print('전역변수 hap 출력:',hap)

#2

hap = 100
num = 50

def sum(value):
    global hap
    hap += value
    print('hap :',hap)
    print('num :',num)
sum(10)
print('hap 출력 :',hap)