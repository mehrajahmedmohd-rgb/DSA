def print_natural(n,N):
    if n>N :
        return 

    print(n)
    print_natural(n+1,N)

N=int(input("enter the numbver :"))
print_natural(1,N)