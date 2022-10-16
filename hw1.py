print ("Input: ",end="")
in1 = input().split(',')
x = {}
pre1 = []
pre2 = []
for i in range (len(in1)):
    in2 = in1[i].split(':')
    x1 = in2[0]
    pre1.append(in2[0])
    y1 = in2[1]
    pre2.append(in2[1])
    x[x1] = y1
f = open('symbols.txt','r')
#fd = open('results.txt','w')
print (x)
while True:
    neko = ""
    peko = f.readline()
    neko = peko
    for i in range (len(pre1)):
        neko = neko.replace(pre1[i], pre2[i])
    print (neko,end = "")
    #fd.write(neko)
    if not peko:
        break
#fd.write("\n")
# *:1,#:2,@:3,$:4