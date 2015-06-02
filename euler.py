from pylab import *
from numpy import *

x = loadtxt('./data/euler_classic.out')
y = loadtxt('./data/euler_swept.out')

figure(figsize=(7,6))
loglog(x[:,0], x[:,1], '--s')
loglog(y[:,0], y[:,1], '-d')

loglog([1,2E2], [100, 5E-1], '-k')
loglog([1E1,1E5], [.5, .5E4], '--k')
ylim([1, 1E4])

legend(['Straight decomposition', 'Swept decomposition'], loc='upper left')

grid(which='minor')
grid(which='major')
xlabel('Spatial points per node $n$')
ylabel('Total time per sub-timestep')
savefig('euler-1d')

xy = loadtxt('./data/ks1d.out')

figure(figsize=(7,6))
loglog(xy[:,0], xy[:,1], '--s')
loglog(xy[:,0], xy[:,2], '-d')

loglog([1,2E2], [200, 1], '-k')
loglog([1E2,1E5], [1, 1E3], '--k')
ylim([1, 1E4])

legend(['Straight decomposition', 'Swept decomposition'], loc='upper left')

grid(which='minor')
grid(which='major')
xlabel('Spatial points per node $n$')
ylabel('Total time per sub-timestep')
savefig('ks-1d')
