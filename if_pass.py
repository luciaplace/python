''' if ~ pass : 조건문에서 아무것도 처리하고 싶지 않을때 사용'''

#1

idum = input("나이를 입력하세요: ")
if int(idum) >= 19:
    pass
else:
    print("신분증을 제시해주세요. ")


#2
pocket = ['money', 'card', 'pen']

if 'money' in pocket :
    pass
else:
    print("카드를 꺼내세요")
