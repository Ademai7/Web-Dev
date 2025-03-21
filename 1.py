a = int(input())
def function(a):
    for i in range(a):
        print(" " * (a - i - 1 ) + "*" * (2 * i + 1))
function(a)

