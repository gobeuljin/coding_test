Base64 = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", \
    11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U",\
        21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z", 26:"a", 27:"b", 28:"c", 29:"d", 30:"e", \
            31:"f", 32:"g", 33:"h", 34:"i", 35:"j", 36:"k", 37:"l", 38:"m", 39:"n", 40:"o",\
                41:"p", 42:"q", 43:"r", 44:"s", 45:"t", 46:"u", 47:"v", 48:"w", 49:"x", 50:"y",\
                    51:"z", 52:"0", 53:"1", 54:"2", 55:"3", 56:"4", 57:"5", 58:"6", 59:"7", 60:"8",\
                        61:"9", 62:"+", 63:"/"}

# world = input()
world = "mis"

ASCII = []

for i in world:
    ASCII.append(str(ord(i))) # 1. ASCII로 변환
print("ascii 로 변환하면 = "+str(ASCII))
 # 2진수로 바꾸기
for i in range(len(ASCII)):
    ASCII[i] = int(ASCII[i])
    ASCII[i] = format(ASCII[i], "b")
print("2진수로 바꾸면 ="+ str(ASCII))
# 2진수를 8bit로 만들기
for i in range(len(ASCII)):
    if len(ASCII[i]) != 8:
        ASCII[i] = "0"*(8-len(ASCII[i]))+ASCII[i]
print(ASCII)

# #3. 6bite 씩 구분하기
str_ascii = "".join(ASCII) # 3. ASCII 문자열을 합침
ASCII.clear()
ASCII = list(str_ascii)

n = (len(ASCII)-1)//6
for i in range(n):
    ASCII.insert((i+1)*6+i, "@")

str_ascii = "".join(ASCII)
str_ascii = str_ascii.split("@")
print(str_ascii)

#마지막 값 6bit로 만들기
if str_ascii[len(str_ascii)-1] !=6:
    str_ascii[len(str_ascii)-1] += "0"*(6-len(str_ascii[len(str_ascii)-1]))
print(str_ascii)

# 4. 6byte 2진수를 10진수로 바꾸기

for i in range(len(str_ascii)):
    str_ascii[i] = int(str_ascii[i], 2)

print(str_ascii)

for i in range(len(str_ascii)):
    str_ascii[i] = Base64[str_ascii[i]]

#5. 완성
str_ascii = "".join(str_ascii)
print(str_ascii)
