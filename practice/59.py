class solution(object):
    def twosum(self,num,target):
        for i in range(len(num)):
            for j in range(i+1 ,len(num)):
                if num[i]+num[j]==target:
                    return [i,j]

        return False

num = list(map(int,input("enter the number:").split()))
target=int(input("enter the number to add:"))
sol = solution()
result = sol.twosum(num,target)
print("Result is" ,result)