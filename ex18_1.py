fr = open('text.txt', 'r')
a = fr.read()
fr.close()
print a

fw = open('test1.txt', 'w')
fw.write(a)
fw.close()


