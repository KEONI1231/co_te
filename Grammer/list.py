"""

    배열과 비슷한 것.
    뭔가 list() 로 선언하는게 더 직관적으로 리스트임을 알리는 거 같다.

    리스트 순회시 음수는 뒤에서 부터 순회
    EX)
    print(a[-1])
    -> 뒤에서 첫 번째 원소 출력

    slicing()
    => 대괄호 안에 콜론(:) 을 넣어서 시작 인덱스와 끝 인덱스를 설정
    => 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정\

    리스트 컴프리헨션
        array = [i for i in range(10)] // i가 0부터 9까지 순회 하는데, 그 i의 값을 array에 넣어주겠다.
        print(array)

        array = [ i for i in range(20) if i % 2 == 1 ]
    2차원 리스트
        N * M
        array = [[0] * m for _ in range(n)]

"""

a = [1,2,3,4,5,6,7,8,9]
print(a)
a.append(1)
print(a)

print(a[3]) #4
print(a[1:4]) #2,3,4

array = [i for i in range(5)]
print(array)
print(array)

array = [[1] * 5 for i in range(5)]
print(array)
b = [[], []]
b[0].append(1)

b[0].append(2)
b[1].append(1)

print(b)
str = "상하좌우문제"
print(str[0])
