a = input()

def function(a):
   if len(a) == 0 :
    return a 
   return a[-1] + function(a[:-1])

print(function(a))