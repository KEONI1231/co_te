#상근이 설탕 문제

kg = int(input())
bag = 0

while(kg >= 0):
    if(kg % 5 == 0) :
        print(bag + int(kg/5))
        break;
    else:
        kg = kg -3
        bag += 1
else :
    print("-1")
