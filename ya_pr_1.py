f = open ('C:/Python/input.txt','r')
file = f.readlines()
n = int(file[0])
if n == 0:
    o = open('C:/Python/output.txt', 'w')
    o.write('')
    o.close()
else:
    idr = list(file[1].split())
    idz = list(file[2].split())
    playlist = []
    for song in range(0,n):
        playlist.append(idr[song])
        playlist.append(idz[song])
    o = open('C:/Python/output.txt','w')
    for index in playlist:
        o.write(index+' ')
    o.close()