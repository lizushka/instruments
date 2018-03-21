#open file, create a new one and create a dictionary
f = open('karamshoev_d_russkishugnanskii_slovar_tom4.txt', 'r')
newf = open('karamshoev_tom4_sorted.txt', 'w')
str = {}

#fill the dictionary, keys are strings nad values are lengthes
for line in f:
    str[line.strip('\n')] = len(line.split())

#sort dictionary keys by values, write keys into new file
for i in sorted(str, key=str.__getitem__):
    newf.write(i + '\n')

#close files
newf.close()
f.close()
