Seq1 = 'ATGTTATAG'
Seq1 = Seq1.replace('A','a')
Seq1 = Seq1.replace('T','A')
Seq1 = Seq1.replace('a','T')
Seq1 = Seq1.replace('C','c')
Seq1 = Seq1.replace('G','C')
Seq1 = Seq1.replace('c','G')

print Seq1

'''Seq1 = 'ATGTTATAG'
newSeq1 = ""
for s in Seq1:
    if s == "A":
        newSeq1 += "T"
    elif s == "C":
        newSeq1 += "G"
    elif s == "G":
        newSeq1 += "C"
    elif s == "T":
        newSeq1 += "A"
print Seq1
print newSeq1'''

'''Seq1 = 'ATGTTATAG'
compSeq = ''
compDic = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
for s in Seq1:
    compSeq += compDic[s]

print Seq1
print compSeq'''
