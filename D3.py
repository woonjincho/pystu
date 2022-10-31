#빈 튜블 선언
t1 = ()

t2 = (1,2,3,4)

t2= (1,"2",'3')

num1,str1,str2 =t2

print(num1,str1,str2)
#--------------------------
#set=집합

s1= set([1,3,5]) #== s1={1,3,5}
s2= {1,3,4,9}

#set 관련 함수

s1.add(8) #값 추가 

s1.update(11,12) #값 여러개 추가

s1.remove(3) #값 삭제

s1.discard(11) #값 삭제(집합에 없는 숫자도 제거 가능=오류 안냄)

#합집합
print(s1|s2)
print(s1.union(s2)) #위랑 똑같은 결과 

#교집합
print(s1 & s2)
print(s1.intersection(s2))

#차집합
print(s1 - s2) 
print(s1.difference(s2))

#대칭차집합
print(s1 ^ s2)

#------------------------------
#내장함수

#sum() -> 합을구함 
arr={2,3,4,5,6}
ar = (2,3,4,5)
print(sum(arr))
print(sum(ar))

#min() -> 최솟값
print(min(arr))

#max() 반대겠지
print(max(arr))

#pow(a,b) -> 거듭제곱
print(pow(6,3))


def test():
    print("응애으야")
test() #위에 프린트는 안나오고 test()만 실행됨

def print_hello(to1,t02):
    print('hello',to1,to2)
print_hello('data','data')