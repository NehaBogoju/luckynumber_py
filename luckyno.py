n=int(input())
def find_lucky(n):
    rem=sum=0
    while n!=0:
        rem=n%10
        sum +=rem
        n //=10
    if sum%2==0:
        return 1
    else:
        return 0
res=find_lucky(n)
if res==1:
    print(n,"is lucky")
else:
    print(n,"is not lucky")