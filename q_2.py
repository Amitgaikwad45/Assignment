# count divisors
def count_divisors(a,b):
    cnt=0
    for i in range(a,b):
        if(i%2==0):
            cnt=cnt+1
    return cnt


x=200
y=300


print(count_divisors(x,y))
