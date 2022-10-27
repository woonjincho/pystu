arr = [1,2,3,4,"안녕",True]

print(range(10)) #range=0~9까지라는뚰

for i in range(2,10,1): #2부터 시작해서 10까지 1까지 증가
    print(i)

#-----------------------
while arr[0] != 1:
    print("arr[0]이 1이면 출력")
print("arr[0]이 1이 아니면 출력")

num =1 
while num ==2:
    print(1)
else:
    print(2)

#-------------------------
#빈 리스트 생성 방법
ar1 = []
ar2 = list(-20,5,1,4)

print(arr[-1]) #-라면 뒤에서 부터 근데 0부터 시작아님 즉 true출력

arr.append(2) #배열에 요소 추가(맨뒤에서 추가댐)

print(len(arr)) #배열의 길이 7

ar3 = [[1,2,3,4],[1,2,3,4]] #이중배열

ar2.sort() #배열정렬

ar2.reverse() #배열 뒤집김

ar2.remove(-20) #요소 없애기(같은 수가 여러개이면 맨앞에꺼 부터 없앰)

pirnt(ar2.count(-20)) #-20의 개수를 출력

ar2.insert(3, -15) #4번쨰에 -15값을 넣음

print(ar2.index(-15)) #-15의 위치 검색
#-------------------------
#빈 딕셔너리 생성
holy ={} 
holy ["운진조"]="01075630813"
holy ["박서영"]="01045798100"

moly={"서영팍":"천재"}

pirnt(holy['박서영'])

del moly["박서영"]