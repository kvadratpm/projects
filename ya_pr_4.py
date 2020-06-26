f = open('C:\Python\input.txt', 'r')
file = f.readlines()
f.close()
m = int(file.pop(0))
mass = [[int(n) for n in string.rstrip().split(' ')] for string in file]
del file
x = m // 2
y = m // 2
s = m - 1
with open('C:\Python\output.txt', 'w') as o:
    for i in range(0, m ** 2):
        o.write(f'{mass[y][x]}\n')
        sum = x + y
        if x <= y:
            if sum <= s:
                y -= 1
            else:
                x -= 1
        elif x > y:
            if sum < s:
                x += 1
            else:
                y += 1
