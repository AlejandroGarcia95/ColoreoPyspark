import random

def myhash(s):
	j = 1
	x = 1
	for c in s:
		x *= ord(c) * j
		x = (x << 5) + 7
	x += (x >> 5)
	x -= (x << 8)- (x >> 5)
	if(x % 19 == 3):
		x ^= (x << 2)
	random.seed(x)
	resultt = (int(random.random() * 191324943.0) % 998909) ^ (x << 1)
	if((resultt % 93 == 3) or (resultt % 93 == 0)):
		resultt = resultt << 1
	return resultt

i=0
col=0
noncol = 0
d=dict()
with open('words.txt') as f:
    for line in f:
        i=i+1
        z = myhash(line) % 400000
        if z in d:
        	col = col + 1
        	d[z]+=1
        else:
        	noncol = noncol+1
        	d[z]=1
print "Number of lines in file: "+str(i)
print "Collisions: " +str(col)
print "Non Collisions: "+str(noncol)
print "Total keys: "+str(col+noncol)
