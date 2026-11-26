string = list(input(""))
line = 15
row = 136
chrs = []
string_length = len(string)
i = 0
k = 0
l = int((row*line-len(string)%(row*line)))
def to_fullwidth(text):
    table = {i: i + 0xFEE0 for i in range(0x21, 0x7F)}  # 所有可见 ASCII
    table[0x20] = 0x3000                                 # 空格特殊
    return text.translate(table)

for space in range(0,l):
    string.append('\u3000')
# print(len(string))
while string_length >0:
    i +=1
    print()
    string_length -= line*row
    for k in range(line):
        for char in string[line*row*(i-1)+k:line*row*i+k:line]:
            chrs.append(char)
        chrs.reverse()
        result = "".join(chrs)
        print(to_fullwidth(result))
        chrs.clear()
        k += 1