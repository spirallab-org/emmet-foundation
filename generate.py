#!/usr/bin/env python

columns = 12

labels = ['large', 'small']

# generate code for each label
for label in labels:
    for i in range(1,columns+1):
        print '"d:' + label[0] + str(i) + '" : "<div class=\\"' + label + "-" + str(i) + ' columns\\">",'
    print # new line
    
print # new line

# generate code for double label
for i in range(1,columns+1):
    for j in range(1,columns+1):
            print '"d:' + labels[0][0] + str(i) + labels[1][0] + str(j) + '" : "<div class=\\"' + labels[0] + "-" + str(i) + " " + labels[1] + "-" + str(j) + ' columns\\">",'
