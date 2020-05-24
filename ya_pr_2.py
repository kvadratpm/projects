f = open('C:/Python/input.txt', 'r')
file = f.readlines()
text = ''.join(file)
if text == '0':
    o = open('C:/Python/output.txt', 'w')
    o.write(text)
    o.close()
else:
    rev_text = ''
    text = text.rstrip('0')
    minus = False
    for i,symbol in enumerate(reversed(text)):
        if symbol == '-':
            minus = True
        else:
            rev_text += symbol
    if minus == True:
        final_text = str(int(rev_text) * (-1))
    else:
        final_text = rev_text
    o = open('C:/Python/output.txt', 'w')
    o.write(final_text)
    o.close()