def spiral(m, matrix):
    result = ''
    x = m // 2
    y = m // 2
    s = m - 1
    for i in range(0, m ** 2):
        result += f'{matrix[y][x]}\n'
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
    return result

f = open('C:/Python/input.txt', 'r')
file = f.readlines()
f.close()
m=int(file.pop(0))
mass = [[int(n) for n in string.rstrip().split(' ')] for string in file]
del file
o = open('C:/Python/output.txt','w')
o.write(spiral(m,mass))
o.close()