''' if ~ elif ~ else
    if 실행조건 :
        조건 만족시 수행문
    elif 실행조건 :
        조건 만족시 수행문
    else:
        위의 모든 조건 불만족시 수행문'''


#1
subject = input("favorite subject:")

if subject =="python":
    print("내가 좋아하는 과목은 파이썬입니다.")
elif subject == "java" :
    print("내가 좋아하는 과목은 자바 입니다.")
elif subject == "C#":
    print("내가 좋아하는 과목은 C#입니다.")
else:
    print("내가 좋아하는 과목은 없습니다.")


#2

shortcut = int(input("단축키를 입력하세요:"))

if shortcut == 1:
    print("엄마 : 010-1111-1111")
elif shortcut == 2:
    print("아빠 : 010-2222-2222")
elif shortcut == 3:
    print("동생 : 010-3333-3333")
else :
    print("해당 단축키가 없습니다.")

#3

month = int(input("월을 입력하세요."))

if month == 12 or month <3 and month>0 :
    print("겨울입니다.")
elif month >2 and month <6 :
    print("봄입니다.")
elif month > 6 and month <9 :
    print("여름입니다.")
elif month >9 and month <12 :
    print("가을입니다.")
else:
    print("입력값이 잘못되었습니다.")

#4

point = int(input("점수를 입력하세요"))

if point <=100 and point >90 :
    print("학점 : A")
elif point <=90 and point >80:
    print("학점 : B")
elif point <=80 and point >70:
    print("학점 : C")
elif point <=70 and point >60:
    print("학점 : D")
elif point <=60 and point >0 :
    print("학점 : F")
else:
    print("입력값이 잘못되었습니다. ")

#5

print("========자판기 메뉴========")
print("1.음료 1000원 2.과자 2000원 3.껌 500원")
print()

cracker = 2000
drink = 1000
ggum =500
money = int(input("Insert Coin: "))

if money >= cracker :
    print("과자, 음료, 껌을 구매할 수 있습니다.")
elif money >= drink:
    print("음료, 껌을 구매할 수 있습니다.")
elif money >= ggum :
    print("껌을 구매할 수 있습니다.")
else:
    print("아무것도 구매할 수 없습니다.")