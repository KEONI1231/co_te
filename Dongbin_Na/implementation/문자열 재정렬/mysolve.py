a = input()

list_str=[]
for i in range(0, len(a)):
    list_str.append(a[i])

list_str.sort()

i = 0
sum_result = 0
while 1:
    if list_str[i].isdigit() == True :
        sum_result += int(list_str[i])
        list_str.pop(0)
    else :
        i = i +1

    if i >= len(list_str) :
        break
list_str.append(sum_result)
for i in list_str :
    print(i, end="")




