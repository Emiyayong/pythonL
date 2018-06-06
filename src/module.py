import sys,pprint,copy,os
#pprint.pprint(sys.path)
#print(copy.copy.__doc__)
'''
args=sys.argv[1:]
args.reverse()
print(''.join(args))
print(os.environ)
pprint.pprint(os.environ)
os.system('~/dev')

import webbrowser
#webbrowser.open('http://www.baidu.com')
import fileinput
print(fileinput.filename())
for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num=fileinput.lineno()
    print('{:<50} # {:2d}'.format(line,num))
'''
from random import shuffle
values=list(range(1,11))+'Jack Queen King'.split()
suits='diamonds hearts clubs spades'.split()
deck=['{} of {}'.format(v,s) for v in values for s in suits]
shuffle(deck)
pprint.pprint(deck[:12])
