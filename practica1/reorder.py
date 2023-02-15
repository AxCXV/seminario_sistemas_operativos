orden = [2, 0, 5, 3, 4, 1]
f = open("prueba2.txt", "r")
out = open("salida.txt", "w")

def hexa_2_dec(num):
    tmp = num.split(":")
    tmp[7] = tmp[7].split("/")[0] 
    for i in range(len(tmp)):
        tmp[i] = int(tmp[i], 16)
    res = ':'.join(map(str, tmp))
    content[1] = res

def dec_2_hexa(num):
    tmp = num.split(".")
    tmp[3] = tmp[3].split('\n')[0]
    for i in range(len(tmp)):
        tmp[i] = hex(int(tmp[i]))
    res = '.'.join(map(str, tmp)) + '\n'
    res = res.upper()
    content[2] = res

for x in f:
    content = x.split(",")
    content = [content[i] for i in orden]
    del content[3:]
    hexa_2_dec(content[1])
    dec_2_hexa(content[2])
    tostring = ' '.join(map(str,content))
    print(tostring)
    out.write(tostring)

f.close()
out.close()