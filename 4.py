n = int(input())  
arr = []  
for _ in range(n):  
    arr.append(int(input()))  

arr.sort()  
evens = []  
odds = []  

for num in arr:  
    if num % 2 == 0:  
        evens.append(num)  
    else:  
        odds.append(num)  

print(*evens, *odds)  
