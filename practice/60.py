class solution(object):
    def two(self,s1,s2):
        frequency_s1={}
        frequency_s2={}

        for char in s1:
            if char in frequency_s1:
                frequency_s1[char]+=1

            else:
                frequency_s1[char] =1

        for char in s2:
            if char in frequency_s2:
                frequency_s2[char]+=1
            else:
                frequency_s2[char]=1

        if frequency_s1 == frequency_s2:
            return True

        return False
s1 = input("enter the string 1: ")
s2 = input("enter the string 2: ")
sol = solution()
result = sol.two(s1,s2)
print(result)
