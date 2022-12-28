s = 'ffttghhhryttttts'

dict_my = {}
count = 0
char = ''
for i in s:
    if i in dict_my.keys():
        dict_my[i] +=1
        if dict_my[i] > count:
            count = dict_my[i]
            char = i

    else:dict_my[i] = 1


print(dict_my)
print(f'{char} = > {count}')
print(dict_my)