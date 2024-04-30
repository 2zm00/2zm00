print("알고싶은 구구단은 무엇인가요?")

user_choice = int(input())

if user_choice>=10:
    for i in range (1,user_choice+1):
        print(user_choice, 'x', i, '=', user_choice*i)
else:
    for i in range (1,10):
        print(user_choice, 'x', i, '=', user_choice*i)

#구구단 1~9단은 9번, 1~n번은 n단까지
#활용해서 html에 연결시키기
#이걸 프로그램화 시키기를 목표로


