print "Let's practice everything."
print "You\'d need to know about escapes with \\ that do \n newLines and \t tabs."
poem = """
\t The lovely world
with logic so frimly planted
cannot discern \n the needs of love
nor comprehend passion from intultion
\n\t\twhere ther is none.
"""
print "-------------------"
print poem
print "-------------------"
five=10-2+3-6
print "This should be five: %s" % five
def secret_formula(started):
   jelly_beans=started*500
   jars=jelly_beans/1000
   crates=jars/100
   return jelly_beans,jars,crates
start_point=10000
bean,jars,crates=secret_formula(start_point)
print "with a starting point of: %d"% start_point
print "we'd have %d beans,%d jars and %d crates."%(bean,jars,crates)
start_point=start_point/10
print "We can also do that this way"
print "We'd have %d beans,%d jars, and %d creats."%(bean,jars,crates)

