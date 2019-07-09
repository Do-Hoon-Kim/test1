'''name = raw_input("Enter name: ")
print 'Hello' + ' ' + name'''

import sys
print(sys.argv)

name = sys.argv[1]
print 'Hello' + ' ' + name
