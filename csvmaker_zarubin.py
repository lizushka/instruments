# -*- coding: utf-8 -*-

import re, codecs

# open file
f = codecs.open('119-135.txt', 'r', 'utf-8')

# create new file
new = codecs.open('119-135.csv', 'w', 'utf-8')

# write heading
new.write('shughni' + '\t' + 'variant' + '\t' 'fem' + '\t' + 'pst' + '\t' + 'pst.f' + '\t' + 'pst.pl' + '\t' + '3sg.npst' + '\t' + 'prf' + '\t' + 'prf.f' + '\t' + 'prf.pl' + '\t' + 'inf' + '\t' + 'plural' + '\t' + 'pl.variant' + '\t' + 'russian' + '\t' + 'example' + '\t' + 'comment' + '\n')

# define types of strings
simple = re.compile(u'([^а-яА-Я]*) ([а-яА-Я]+?.*?)$')

examples = re.compile(u'([^а-яА-Я]*) ([а-яА-Я]+?.*?); (.+)$')

verbs = re.compile(u'([^а-яА-Я]*): ?([^а-яА-Я]*) ([а-яА-Я]+?.*?)$')

verbs_examples = re.compile(u'([^а-яА-Я]*): ?([^а-яА-Я]*) ([а-яА-Я]+?.*?); (.+)$')

# separate lines of the documnt by types, write lines into new file
for line in f:
    a = verbs_examples.match(line)
    if a is not None:
        new.write(a.group(1) + '\t' + '\t' + '\t' + a.group(2) + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + a.group(3) + '\t' + a.group(4).strip('\n') + '\t' + '\n')
    else:
        b = verbs.match(line)
        if b is not None:
            new.write(b.group(1) + '\t' + '\t' + '\t' + b.group(2) + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + b.group(3).strip('\n') + '\t' + '\n')
        else:
            c = examples.match(line)
            if c is not None:
                new.write(c.group(1) + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + c.group(2) + '\t' + c.group(3).strip('\n') + '\t' + '\n')
            else:
                d = simple.match(line)
                if d is not None:
                    new.write(d.group(1) + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + d.group(2).strip('\n') + '\t' + '\t' + '\n')
                else:
                    new.write(line + '\n')

#close files
new.close()
f.close()
