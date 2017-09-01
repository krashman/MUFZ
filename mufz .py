#python 2.7

import time, sys

print "\n" + " "*7 + "Mobile Unicode Fuzzing Framework"
print(" "* 19 + "By ZADEW!\n")
print "=" * 47
print"\n"
time.sleep(2)
current_time = time.time()

laggy = []

for i in range(1,65535): 
	starttime = time.time()
	print i, "", unichr(i), #chr for 3.5
	endtime = time.time()
	lag = endtime - starttime
	print lag
	if lag >= 0.15: #customize 
		laggy.append(i)

print""
print""

print laggy[:]

print "\n[*] ",
print str(len(laggy)), 
print " Dangerous Chars found in"
print "  --- %s seconds ---" % (time.time() - current_time)

sys.exit()
