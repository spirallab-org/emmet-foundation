#!/usr/bin/env python

columns = 12

sizes = ['small', 'large']

######################################
# block grid code

# generate code for each size
for size in sizes:
    for i in range(1,columns+1):
        print '"d:' + size[0] + str(i) + '" : "<div class=\\"' + size + "-" + str(i) + ' columns\\">",'
    print # new line
    
print # new line

# generate code for double size
for i in range(1,columns+1):
    for j in range(1,columns+1):
            print '"d:' + sizes[0][0] + str(i) + sizes[1][0] + str(j) + '" : "<div class=\\"' + sizes[0] + "-" + str(i) + " " + sizes[1] + "-" + str(j) + ' columns\\">",'

print # new line

######################################
# block grid code

# generate code for each size
for size in sizes:
    for i in range(1,columns+1):
        print '"u:' + size[0] + str(i) + '" : "<ul class=\\"' + size + "-block-grid-" + str(i) + '\\">",'
    print # new line
    
print # new line

# generate code for double size
for i in range(1,columns+1):
    for j in range(1,columns+1):
            print '"u:' + sizes[0][0] + str(i) + sizes[1][0] + str(j) + '" : "<ul class=\\"' + sizes[0] + "-block-grid-" + str(i) + " " + sizes[1] + "-block-grid-" + str(j) + '\\">",'