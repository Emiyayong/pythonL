'a test module'
__author__="gouyong"
import sys
def test():
   args=sys.argv
   if len(args)==1:
       print("Hello World!")
   elif len(args)==2:
       print("Hello %s!",args[1])
   else:
       print("too many arguments!")
if __name__=='__mian__':
    test(1)

