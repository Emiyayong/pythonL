f=open('somefile.txt')
lines=f.readlines();
f.close()
lines[1]="isn't a\n"
f=open(r'somefile.txt','w')
f.writelines(lines)
f.close()

