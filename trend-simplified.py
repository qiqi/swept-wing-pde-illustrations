from pylab import *
from numpy import *

figure()

n = array([1, 1E7])

s = [10 / 11.6E12, 200 / 11.6E12, 4000 / 11.6E12, 10 / 10E9, 200 / 10E9, 4000 / 10E9]
print s
sLabel = ['Dual R9 290X, 10 FLOP/step', 'Dual R9 290X, 200 FLOP/step',
          'Dual R9 290X, 4000 FLOP/step', 'Haswell core, 10 FLOP/step',
          'Haswell core, 200 FLOP/step', 'Haswell core, 4000 FLOP/step']

t = [0.7E-6, 5E-6, 50E-6, 400E-6]
tLabel = ['Infiniband', '100Gb Ethernet', '1Gb Ethernet', 'Amazon EC2']

linesComp = []
for si in s:
    linesComp.append(loglog(n, n * si, '--')[0])

legendComp = legend(reversed(linesComp), reversed(sLabel), loc='upper right')

linesComm = []
for ti in t:
    linesComm.append(loglog(n, 2 * ti / n, '-')[0])

legendComm = legend(reversed(linesComm), reversed(tLabel), loc='upper left')

grid(which='minor')
gca().add_artist(legendComm)
gca().add_artist(legendComp)
xlabel('Spatial points per node')
ylabel('Computing time per sub-timestep')
savefig('trend-simplified')
