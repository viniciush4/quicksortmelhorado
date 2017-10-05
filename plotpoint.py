from numpy import *
import matplotlib.pyplot as plt
def comp(n):
	return 2*n*log(n) - 1.846*n

def comp2(n,m):
	return (n+1)*( 1. + (m*(m-1))/(6*(m+2)) + 2*(log(n+1) - log(m+2)))

def comp3(n):
	return (n*(n-1))/4

def plot(points,N,M):
	plt.figure()
	x1 = arange(1.,M+1,10.)
	y1 = comp3(x1)

	x2 = arange(M+1,N+1,10.)
	y2 = comp2(x2,M)

	x3 = arange(1.,N+1,10.)
	y3 = comp(x3)

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

	ll = plt.plot(x1,y1,'y-',linewidth = 8,label = 'Comparacoes teoricas')
	plt.plot(x2,y2,'y-',linewidth = 8)
	plt.plot(x3,y3,linewidth = 3,label = '2N*ln(n) - 1.846*N')
	plt.plot(range(1000,N+1,1000),ll2,'-ro',label = 'Mean of 100')
	xl = plt.xlabel('Problem size (length of array to be sorted)')
	yl = plt.ylabel('Cost (QuickSort Compares)')
	ttl = plt.title('QuickSort + InsertionSort M=' + str(M))
	#ax = plt.axis([500., N+500,comp3(500),comp2(N+1000,M)])
	grd = plt.grid(True)
	ll = plt.legend(loc='lower right')
	#plt.show()
	plt.savefig("graphic%d.png"%(M), dpi = 500)
