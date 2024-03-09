n, k = map(int, input().split())

result = 0;
target = 0;
while True:
    if n % k == 0 :
        result = result + 1
        n = n // k
    else :
        n = n - 1
        result += 1
    if n == 1 :
        break

print(result)