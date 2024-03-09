number = (input())
result = 0;
i = 0;
while i < len(number):
    if(int(number[i]) == 0 or int(number[i]) == 1 or result == 0):
        result += int(number[i])
    else :
        result = result * int(number[i])

    i += 1
print(result)