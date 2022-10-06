print("박서영바보 ㅋㅋ");
print(12+12);
print("박서영"+"바보");
print("박서영바보"*10);
print("더하기를 하시오",10+10);
print("곱하기를 하시오",10*10);
print("나누기를 하시오",10/10);
print("%d+%d=%d" % (123,123,123+123));
#--------------------
name="조운진"
print(name)

print("안녕하세요"[2])
#---------------------
num=int(input("숫자 : "))
print(num)
#int 쓰는게 더 정확함 그냥하셈
num2=input("문자:")
print(num2)
#--------
#파이썬은 들여쓰기를 야무지게 해야함
t1 = False
t2 = True

if t1:
    print("1실행")
elif t2:
    print("2실행")
else :
    print("else실행")

#------------------------
t1 = False
t2 = True

if not(t2 and t1):
    print("and실행")