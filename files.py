f = open('output.txt', 'w', encoding='utf-8')
f.write('bla')
f.close()

r = open('output.txt')
line = r.read()
print(line)
r.close()

