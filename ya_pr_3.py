from typing import List

f = open('C:/Python/input.txt', 'r')
file = f.readlines()
text = ''.join(file)
numbers = text.split()
if text == '0':
    o = open('C:/Python/output.txt', 'w')
    o.write(text)
    o.close()
else:
    n = int(numbers.pop(0))
    full = [x for x in range(1, n + 1)]
    nofull = [int(item) for item in numbers]
    x = sorted(list(set(full) - set(nofull)))
    result = ' '.join(str(i) for i in x)
    o = open('C:/Python/output.txt', 'w')
    o.write(result)
    o.close()
