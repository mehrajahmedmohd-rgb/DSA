def subsequence(s,index,current):
    if index == len(s):
        print(current)
        return

    
    subsequence(s,index+1,current+s[index])
    subsequence(s,index+1,current)


s = input("Enter a string: ")
subsequence(s, 0, "")