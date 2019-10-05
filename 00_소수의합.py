#입력으로 주어진 수 n까지의 소수(prime number)의 합을 리턴하시오.

def prime(n):
    sumcount=0
    count=0
    for i in range(2,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            sumcount+=1
    return sumcount

print(prime(100))
# 2+3+5+7