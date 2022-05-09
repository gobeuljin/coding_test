Base64 = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", \
    11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U",\
        21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z", 26:"a", 27:"b", 28:"c", 29:"d", 30:"e", \
            31:"f", 32:"g", 33:"h", 34:"i", 35:"j", 36:"k", 37:"l", 38:"m", 39:"n", 40:"o",\
                41:"p", 42:"q", 43:"r", 44:"s", 45:"t", 46:"u", 47:"v", 48:"w", 49:"x", 50:"y",\
                    51:"z", 52:"0", 53:"1", 54:"2", 55:"3", 56:"4", 57:"5", 58:"6", 59:"7", 60:"8",\
                        61:"9", 62:"+", 63:"/"}
rev_Base64 = dict(map(reversed,Base64.items()))

t = int(input())

for e in range(1, t+1):
    world = input()
    decording = []

    for i in world:
        decording.append(rev_Base64[i])

    for i in range(len(decording)):
        decording[i] = int(decording[i])
        decording[i] = format(decording[i], "b")

    for i in range(len(decording)):
        if len(decording[i]) != 6:
            decording[i] = "0"*(6-len(decording[i]))+decording[i]

    str_ascii = "".join(decording)
    decording.clear()
    decording = list(str_ascii)

    n = (len(decording)-1)//8
    for i in range(n):
        decording.insert((i+1)*8+i, "@")

    str_ascii = "".join(decording)
    str_ascii = str_ascii.split("@")


    for i in range(len(str_ascii)):
        str_ascii[i] = int(str_ascii[i], 2)

    for i in range(len(str_ascii)):
        str_ascii[i] = chr(str_ascii[i])

    decording = "".join(str_ascii)
    print("#{0} {1}".format(e, decording))