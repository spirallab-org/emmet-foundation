#!/usr/bin/env python

columns = 12

sizes = ['small', 'large']

######################################
# file header
print '''
{
    "variables": {
        "lang": "en",
        "locale": "en-US",
        "charset": "UTF-8",
        "indentation": "\\t",
        "newline": "\\n"
    },
    
    "html": {
        "filters": "html",
        "profile": "html",
        "snippets": {
        },
        
        "abbreviations": {
            "d:r" : "<div class=\\"row\\">",
'''
######################################
# block grid code

# generate code for each size
for size in sizes:
    for i in range(1,columns+1):
        for centered in [""]+[size]:
            if centered:
                centered = centered + "-centered "
                prefix = "c"
            else:
                prefix = ""
            print '\t\t\t"d:' + size[0] + str(i) + prefix + '" : "<div class=\\"' + size + "-" + str(i) + ' ' + centered +'columns\\">",'
    print # new line
    
print # new line

# generate code for double size
for i in range(1,columns+1):
    for j in range(1,columns+1):
        print '\t\t\t"d:' + sizes[0][0] + str(i) + sizes[1][0] + str(j) + '" : "<div class=\\"' + sizes[0] + "-" + str(i) + " " + sizes[1] + "-" + str(j) + ' columns\\">",'
        print '\t\t\t"d:' + sizes[0][0] + str(i) + "c" + sizes[1][0] + str(j) + '" : "<div class=\\"' + sizes[0] + "-" + str(i) + " small-centered " + sizes[1] + "-" + str(j) + ' columns\\">",'
        print '\t\t\t"d:' + sizes[0][0] + str(i) + sizes[1][0] + str(j) + "c" + '" : "<div class=\\"' + sizes[0] + "-" + str(i) + " " + sizes[1] + "-" + str(j) + ' large-centered columns\\">",'
        print '\t\t\t"d:' + sizes[0][0] + str(i) + "c" + sizes[1][0] + str(j) + "c" + '" : "<div class=\\"' + sizes[0] + "-" + str(i) + " small-centered " + sizes[1] + "-" + str(j) + ' large-centered columns\\">",'
            

print # new line

######################################
# block grid code

# generate code for each size
for size in sizes:
    for i in range(1,columns+1):
        print '\t\t\t"u:' + size[0] + str(i) + '" : "<ul class=\\"' + size + "-block-grid-" + str(i) + '\\">",'
    print # new line
    
print # new line

# generate code for double size
for i in range(1,columns+1):
    for j in range(1,columns+1):
            print '\t\t\t"u:' + sizes[0][0] + str(i) + sizes[1][0] + str(j) + '" : "<ul class=\\"' + sizes[0] + "-block-grid-" + str(i) + " " + sizes[1] + "-block-grid-" + str(j) + '\\">",'
######################################
# file footer
print '''
        }, 
    },
}
'''