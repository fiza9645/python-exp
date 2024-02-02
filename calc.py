a=int(input("enter the 1st no:"))
b=int(input("enter the 2nd no:"))
print("1.+ 2.- 3.* 4./ 5.%")
n=int(input("Enter your choice:"))
if n==1:
    s=a+b
    print(s)
elif n==2:
    d=a-b
    print(d)
elif n==3:
    m=a*b
    print(m)
elif n==4:
    div=a/b
    print(div)
elif n==5:
    mod=a%b
    print(mod)
else:
    print("incorrect choice")