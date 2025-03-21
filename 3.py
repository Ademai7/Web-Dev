n = int(input())
arr = list(map(int, input().split()))
arr.sort()


evens = [num for num in arr if num % 2 == 0]
odds = [num for num in arr if num % 2 != 0]

print(*evens, *odds)
