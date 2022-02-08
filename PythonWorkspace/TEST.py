f=open("test.txt",'w')
f.write("Life is too short\nYou need java")
f.close()

f=open("test.txt",'r')
words=f.read().split()

for i in range(len(words)):
    if words[i] == "short":
        words[i] += '\n'
    elif words[i] == "java":
        words[i] = "python"

print(words)
f.close()

f=open("test.txt",'w')
for j in words:
    if j != "short\n":
        j += ' '

f.write(j)
f.close()

