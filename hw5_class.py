
class Node():
	def __init__ (self):
		self.x = 0
		self.y = 0
		self.pts = None
		self.rew = 0.0
		self.util = 0.0
		self.delta = 100
		self.parent = None

def valueIt(spacemat,rows,cols,tol):	
	err = 100
	while err > tol:
		err = 0
		for i in range(0,cols):
			for j in range(rows,0,-1):
				u1 = spacemat[i][j].util
				if spacemat[i][j].rew == 50:
					spacemat[i][j].util = 50 
					spacemat[i][j].delta = 0
				else:
					a = b = c = d = 0
					#left
					if(i-1 >= 0 and spacemat[i-1][y].pts != 2):
						a = a  + 0.1 * spacemat[i-1][j].util
						b = b + 0.1 * spacemat[i-1][j].util
						d = d + 0.8 * spacemat[i-1][j].util
					
					else:
						d = d - 1000
						if(j+1 < rows and spacemat[i][j+1].pts != 2):
							a = a + 0.1 * spacemat[i][j+1].util
						if(j-1 < rows and spacemat[i][j-1].pts != 2):
							b = b + 0.1 * spacemat[i][j-1].util
					#up
					if(j+1 < rows and spacemat[i][j+1].pts != 2):
						a = a + 0.8 * spacemat[i][j+1].util
						c = c + 0.1 * spacemat[i][j+1].util
						d = d + 0.1 * spacemat[i][j+1].util
					else:
						a = a - 1000
						if(i+1 < cols and spacemat[i+1][j].pts != 2):
							c = c + 0.1 * spacemat[i+1][j].util
						if(i-1 < cols and spacemat[i-1][j].pts != 2):
							d = d + 0.1 * spacemat[i-1][j].util
					#right
					if(i+1 < cols and spacemat[i+1][j].pts != 2):
						a = a + 0.1 * spacemat[i+1][j].util
						b = b + 0.1 * spacemat[i+1][j].util
						c = c + 0.8 * spacemat[i+1][j].util
					else:
						c = c - 1000
						if(j+1 < rows and spacemat[i][j+1].pts != 2):
							a = a + 0.1 * spacemat[i][j+1].util
						if(j-1 < rows and spacemat[i][j-1].pts != 2):
							b = b + 0.1 * spacemat[i][j-1].util
					#down
					if(j-1 >=0 and spacemat[i][j-1].pts != 2):
						b = b + 0.8 * spacemat[i][j-1].util
						c = c + 0.1 * spacemat[i][j-1].util
						d = d + 0.1 * spacemat[i][j-1].util
					else:
						b = b - 1000
						if(i+1 < cols and spacemat[i+1][j].pts != 2):
							c = c + 0.1 * spacemat[i+1][j].util
						if(i-1 < cols and spacemat[i-1][j].pts != 2):
							d = d + 0.1 * spacemat[i-1][j].util
					
					spacemat[i][j].util = (spacemat[i][j]).rew + 0.9 * max(a,b,c,d)
					
					u2 = (spacematrix[i][j]).util
					temp = abs(u2 - u1)
					if(temp < spacemat[i][j].delta):
						spacemat[i][j].delta = temp
					if spacemat[i][j].delta > err:
						err = spacemat[i][j].delta
	return spacemat
