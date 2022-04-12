#ascii to binary
chara=str(input())
bina=""
for c in chara:
    ascival=ord(c)
    #print(ascival," ")
    li=""
    bin=0
    for i in range(8):
        bin*=10
        bin+=ascival%2
        ascival=ascival//2
    li+=str(bin)
    
    bit=li[::-1]
    bina+=bit
    
print(bina)
