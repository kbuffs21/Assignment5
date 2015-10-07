from sys import argv
import math
from hw5_class import *

script, world, tol = argv

matrix = []
with open ( world , 'r') as tm:
	for line in tm:
		line = line.strip()
		if len(line) > 0:
			matrix.append(map(int, line.split()))
rows = len(matrix)-1
cols = len(matrix[0])-1

spacemat = []                
for i in range (0, cols): 
    new = []            
    for j in range (0,rows):
        new.append(0) 
    spacemat.append(new) 

for i in range(0,cols):
	for j in range(0,rows):
		print i
		print j
		space = Node()
		space.x = i
		space.y = j
		val = matrix[i][j]
		space.pts = val			
		if val == 1:
			space.rew =(-1)
		elif val == 2:
			space.rew = (-10)
		elif val == 3:
			space.rew = (-2)
		elif val == 4:
			space.rew = 1
		elif val == 50:	
			space.rew = 50
		spacemat[i][j] = space	
		
spacemat = valueIt(spacemat,rows,cols,tol)

closed = []
closed.append("("+str(rows)+","+str(0)+")"+", "+str(spacemat[0][cols].util))

while(spacemat[i][j].rew != 50):
		if(i-1 >=0 and spacemat[i-1][j].Type != 2):
			a = spacemat[i-1][j].util
		else:
			a = -1000
		if(j+1 < rows and spacemat[i][j+1].pts != 2):
			b = spacemat[i][j+1].util
		else:
			b = -1000
		if(i+1 < cols and space[i+1][j].pts != 2):
			c = matrix[i+1][j].util
		else:
			c = -1000
		if(j-1 >=0 and space[i][j-1].pts != 2):
			d = spacemat[i][j-1].util
		else:
			d = -1000
		n = max(a,b,c,d)
		if n == a:
			closed.append("("+str(i-1)+","+str(j)+"), "+str(spacemat[i-1][j].util))
			spacemat[i-1][j].parent = spacemat[i][j]
			i = i - 1
		if n == b:
			closed.append("("+str(i)+","+str(j+1)+"), "+str(spacemat[i][j+1].util))
			spacemat[i][j+1].parent = spacemat[i][j]
			j = j + 1
		if n == c:
			closed.append("("+str(i+1)+","+str(j)+"), "+str(spacemat[i+1][j].util))
			spacemat[i+1][j].parent = spacemat[i][j]
			i = i + 1
		if n == d:
			closed.append("("+str(i)+","+str(j-1)+"), "+str(spacemat[i][j-1].util))
			spacemat[i][j-1].parent = spacemat[i][j]
			j = j - 1
		else:
			print 0
print path
		

