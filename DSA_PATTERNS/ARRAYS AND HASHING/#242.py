class solution(object):
    def leet(self,s,t):
        frequency_s = {}
        frequency_t={}
        for char in s:
            if char in frequency_s:
                frequency_s[char]+=1
            else:
                frequency_s[char] = 1

        for char in t:
            if char in frequency_t:
                frequency_t[char] +=1
            else:
                frequency_t[char] = 1

        if frequency_s == frequency_t:
            return True

        return False


s = input("enter the string 1: ")
t = input("enter the string 2: ")
sol = solution()
result = sol.leet(s,t)
print(result)