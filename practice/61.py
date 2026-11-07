class solution(object):
    def group_anadram(self,sen):
        group={}
        for char in sen:
            key="".join(sorted(char))
            if key in group:
                group[key].append(char)
            else:
                group[key]=[char]
        return list(group.values())

sen=input("enter the sentence: ")
sol=solution()
result=sol.group_anadram(sen)
print(result)