''' 함수 :
    def 함수이름 ( 매개변수 ) :
        함수 내용 작성 '''

#1
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiple(a,b):
    return a*b

def divide(a,b):
    return a/b

a = int(input('첫번째 수를 입력하세요'))
b = int(input('두번째 수를 입력하세요'))

print(multiple(a,b))

#2 구구단

def gugudan(dan):
    for val in range(1,10):
        print("%d * %d = %d" %(dan,val,dan*val))

dan = int(input("단을 입력하세요."))
gugudan(dan)

#3

id = 'python'
pw ='python123'

def account(userid, userpw):
    if id == userid:
        if pw == userpw:
            print("로그인이 되었습니다.")
        else:
            print("비밀번호가 맞지 않습니다.")
    else:
        print("아이디가 맞지 않습니다.")

userid = input("아이디를 입력하세요")
userpw = input("비밀번호를 입력하세요")

account(userid, userpw)