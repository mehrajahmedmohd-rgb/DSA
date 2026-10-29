def hanoi(n,start,helper,destination):
    if n == 1:
        print(f"move disk one from {start} to {destination}")
        return 

    hanoi(n-1,start,destination,helper)

    print(f"move disk {n} from {start} to {destination}")


    hanoi(n-1,helper,start,destination)

n=int(input("enter the hanooi number"))
hanoi(n,"A","B","C")
