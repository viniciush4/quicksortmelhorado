from numpy import *
import matplotlib.pyplot as plt
def comp(n):
	return 2*n*log(n) - 1.846*n

def comp2(n,m):
	return 2*(n+1)*(log(n+1)-log(m+1))+ (m*(m-1)*(n+1))/(4*(m+1))

def plot(points,N):
	x = arange(1000.,N+1,400.)
	y = comp2(x,2)

	i=0
	sm = 0
	ll2 = []
	plt.scatter(0,0,label = 'Experiment')
	for point in points:
		plt.scatter(*point,color='0.20')
		sm += float(point[1])
		i+=1
		if(i == 100):
			ll2 += [sm/100.]
			sm = 0
			i=0

	ll = plt.plot(x,y,'y-',linewidth = 8,label = 'Comparacoes teoricas')
	plt.plot(range(1000,N+1,1000),ll2,'-ro',label = 'Mean of 100')
	xl = plt.xlabel('Problem size (length of array to be sorted)')
	yl = plt.ylabel('Cost (QuickSort Compares)')
	ttl = plt.title('QuickSort')
	ax = plt.axis([500., N+500,comp(500),comp(N+1000)])
	grd = plt.grid(True)
	ll = plt.legend(loc='lower right')
	plt.show()
