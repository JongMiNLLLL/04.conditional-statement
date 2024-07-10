# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력 받아 학점으로 환산하여 출력하라
score = int(input("학점을 입력하시오."))
if score <= 20 :
    print("E")
elif score <= 40 :
    print("D")
elif score <= 60 :
    print("C")
elif score <= 80 :
    print("B")
else :
    print('A')
