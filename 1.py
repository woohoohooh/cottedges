a = []
with open('1.txt', 'r', encoding='utf8') as f:
    for i in f:
        if i.lower().strip() not in a:
            a.append(i.lower().strip())
for i in a:
    print(i.strip())

