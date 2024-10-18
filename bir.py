# 4 masala
"""
f = open("bir.txt", "r")
a = f.read()
b = a.split(" ")
f.close()



for i in b:
    if i[0].isupper():
        print(i)
"""

# 5 masala
"""
f = open("ikki.txt", "r")
a = f.read()
b = a.split(" ")
f.close()



for i in b:
    if len(i)==3:
        print(i)
"""

# 6 masala
"""
f = open("ikki.txt", "r")
a = f.read()
b = a.split(" ")
f.close()



for i in b:
    if len(i) >= 4:
        print(i)
"""

# 7 masala

s=0
f = open("2_qism.txt", "a")
n = int(input())
if n%2==1:
    for i in range(1,n+1):
        s = str(i ** 2)
        for x in range(1,i+1):
            if x != i:
                print()

        print("s = ",s)
        f.write()
else :
    for i in range(n,0,-1):
        s = str(i ** 2)+ "\n"
        print("s = ", s)
        f.write(s)
f.close()
