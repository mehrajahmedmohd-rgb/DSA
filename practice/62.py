def group_anadram(sen):
    group = {}
    for char in sen:
        key = "".join(sorted(char))
        if key in group:
            group[key].append(char)
        else:
            group[key]=[char]
    return list(group.values())

sen = input("enter the number: ")
result = group_anadram(sen)
print(result)