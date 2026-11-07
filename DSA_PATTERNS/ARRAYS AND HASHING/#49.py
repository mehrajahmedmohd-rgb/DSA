def group_anagram(sentence):
    group = {}
    for word in sentence:
        key="".join(sorted(word))
        if key in group:
            group[key].append(word)
        else:
            group[key]=[word]

    return list(group.values())

sentence=input("enter the sentence:")
print(group_anagram(sentence))