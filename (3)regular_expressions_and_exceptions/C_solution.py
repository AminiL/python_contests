import re
s = input()
if len(s) < 4:
    print("ERROR")
    exit()

if s[-1] == '\n':
    s = s[0: -1]

if s[0] == '#':
    if len(s) != 7:
        print("ERROR")
        exit()
    ans = []
    for i in range(1, len(s), 2):
        num = 0
        try:
            num = int(s[i: i + 2], 16)
        except Exception:
            print("ERROR")
            exit()
        if num >= 0 and num < 256:
            ans.append(num)
        else:
            print("ERROR")
            exit()
    for x in ans:
        print(x, end=' ')
    exit()

s = re.sub(' ', '', s)


def ans(s, per=False):
    lst = s.split(',')
    if len(lst) != 3:
        return []
    for x in lst:
        dec = 0
        try:
            dec = int(x)
        except Exception:
            return []
        else:
            if per is True:
                if dec < 0 or dec > 100:
                    return []
                continue
            if dec < 0 or dec > 255:
                return []
    return lst

if s[0] >= '0' and s[0] <= '9':
    lst = ans(s)
    if len(lst) == 0:
        print("ERROR")
        exit()
    for x in lst:
        print(x, end=' ')
    exit()

h = re.search('[rgb][rgb][rgb]\([0-9]+%*,[0-9]+%*,[0-9]+%*\)', s)
if h is None:
    print("ERROR")
    exit()

new_s = h.group(0)
if new_s != s:
    print("ERROR")
    exit()
perc = False
cnt = s.count('%')
if cnt != 0:
    if cnt != 3:
        print("ERROR")
        exit()
    perc = True
    s = re.sub('%', '', s)

m = {}
for i in range(3):
    m[s[i]] = i

s = re.sub('[rgb\(\)]', '', s)
lst = ans(s, perc)
if len(lst) == 0:
    print("ERROR")
    exit()
s = "rgb"

if perc is True:
    for x in s:
        if m.get(x) is None:
            print("ERROR")
            exit()
    for x in s:
        print((int(lst[m[x]]) * 255) // 100, end=' ')
else:
    for x in s:
        if m.get(x) is None:
            print("ERROR")
            exit()
    for x in s:
        print(lst[m[x]], end=' ')
