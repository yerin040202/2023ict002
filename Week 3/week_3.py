# -*- coding: utf-8 -*-
"""Week 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QBGPEb502WHG0bD5OHwgIx4hqLUAAe4H
"""

a=10
a+=5
print(a)

str1="Python"
str2="Programming"
str3="is"
str4="a amazing Language."
print(str1,str2,str3,str4)
print(str1 + " " + str2 + " " + str3 + " " + str4)

str1="Python"
str2="Programming"
str3="is"
str4="a amazing Language."
str1 += " " + str2 + " " + str3 + " " + str4
print(str1)

a=10
b=5
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

a=100
b=200
print(a<b and a==110)
print(a==100 and a<b)

kor=90
eng=80
math=100
kor>=80 and eng>=80 and math>=80

kor=90
eng=80
math=100
CUT_OFF=80

cond1 = kor >= CUT_OFF                   # 코멘트 ㅎ.,ㅎ
cond2 = eng >= CUT_OFF
cond3 = math >= CUT_OFF

print(cond1 and cond2 and cond3)

print(bin(12))
print(oct(12))
print(hex(12))

num1=125 
num2=100 
num3=120
max=num1 if num1>num2 else num2
max=num3 if num3>max else max
print("가장 큰 값",max)

num1, num2, num3 = map(int, input().split())
max=num1 if num1>num2 else num2
max=num3 if num3>max else max
print("가장 큰 값",max)

num=int(input("어떤 숫자: "))
remainder=num%3
출력값="입니다" if remainder==0 else "가 아닙니다"
print("당신이 입력한 숫자",num,"는(은) 3의 배수",출력값)

num=int(input("어떤 숫자: "))
result= "입니다." if num%3==0 else "가 아닙니다."
print(f"당신이 입력한 숫자 {num}는(은) 3의 배수 {result}")

price=int(input("상품 가격? "))
result= "True" if price>=60000 else "False"
print(f"할인 대상 : {result}")

age=int(input("나이?: "))
출력값="있습니다." if age>=20 else "가 아닙니다"
print("이 등급의 영화를 볼 수",출력값)

"""**수행평가**"""

alp=input("알파벳을 입력하세요: ")
출력값="대문자 입니다." if alp.isupper() else "소문자 입니다"
print(f"당신이 입력한 문자 {alp}는 {출력값}")

"""**if 조건문**"""

학점=float(input("이번 학기 학점 : "))
if 학점>=4.0:
    print(f"장학금 신청 대상")
else:
    print(f"장학금 학점 미달")

num=float(input("어떤 수? "))
if num%2==0:
    print(f"입력한 수 {num}은 짝수이다.")
else:
    print(f"입력한 수 {num}은 홀수이다.")