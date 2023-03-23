import string
alpha = list(string.ascii_lowercase)
se = []
y = int(input())
x = str(input()).lower()

for i in range(0,len(x)):
    se.append(x[i])
a = set(se)
b = sorted(list(a))

if (len(a)==len(alpha)):
    print("YES")
else:
    print("NO")