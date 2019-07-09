fr = open('text.txt', 'r')

a = fr.readlines()

for r in a:
    print r.strip()
fr.close()
