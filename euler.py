from pylab import *
from numpy import *

x = loadtxt('./data/euler_classic.out')
y = loadtxt('./data/euler_swept.out')

figure(figsize=(7,6))
loglog(x[:,0], x[:,1], '--o')
loglog(y[:,0], y[:,1], '-d')

legend(['Straight decomposition', 'Swept decomposition'], loc='upper left')

grid(which='minor')
xlabel('Spatial points per node $n$')
ylabel('Total time per sub-timestep')
savefig('euler-1d')
