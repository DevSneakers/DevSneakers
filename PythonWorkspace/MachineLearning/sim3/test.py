lines = ['Hello\n', 'This file\n']

f = open("myfile.txt", 'w')

for line in lines:
    f.write(line)

f = open("myfile.txt", 'r')
lines = f.read().split('\n')

print(lines)