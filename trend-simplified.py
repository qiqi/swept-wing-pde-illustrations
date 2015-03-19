from pylab import *
from numpy import *

n = exp(linspace(log(1), log(1E7), 71))

s = [3 / 40E12, 200 / 40E12, 4000 / 40E12, 3 / 10E9, 200 / 10E9, 4000 / 10E9]
print(s)
sLabel = ['Summit node, 3 FLOP/step', 'Summit node, 200 FLOP/step',
          'Summit node, 4000 FLOP/step', 'Nehalem core, 3 FLOP/step',
          'Nehalem core, 200 FLOP/step', 'Nehalem core, 4000 FLOP/step']

t = [0.7E-6, 5E-6, 50E-6, 150E-6]
tLabel = ['Infiniband', '100Gb Ethernet', '1Gb Ethernet', 'Amazon EC2']
tColor = ['r', 'g', 'b', 'k']

# ---------------------- swept 1d ------------------------- #
figure()

for si in s:
    for ti in t:
        loglog(n, n * si + 2 * ti / n, '-', color='#444444')

linesComp = []
for si in s[:3]:
    linesComp.append(loglog(n, n * si, '--', lw=3)[0])
for si in s[3:]:
    linesComp.append(loglog(n, n * si, '-.', lw=3)[0])

legendComp = legend(reversed(linesComp), reversed(sLabel), loc='upper right')

linesComm = []
for ti, ci in zip(t, tColor):
    linesComm.append(loglog(n, 2 * ti / n, '-' + ci, lw=3)[0])
    loglog(2, ti, 'o' + ci)

legendComm = legend(reversed(linesComm), reversed(tLabel), loc='upper left')

grid(which='minor')
gca().add_artist(legendComm)
gca().add_artist(legendComp)
xlabel('Spatial points per node $n$')
ylabel('Total time per sub-timestep')
savefig('trend-simplified-1d')

# ---------------------- swept 2d ------------------------- #
figure()

for si in s:
    for ti in t:
        loglog(n, n * si + 4 * ti / n**(1./2), '-', color='#444444')

linesComp = []
for si in s[:3]:
    linesComp.append(loglog(n, n * si, '--', lw=3)[0])
for si in s[3:]:
    linesComp.append(loglog(n, n * si, '-.', lw=3)[0])

legendComp = legend(reversed(linesComp), reversed(sLabel), loc='lower left')

linesComm = []
for ti, ci in zip(t, tColor):
    linesComm.append(loglog(n, 4 * ti / n**(1./2), '-' + ci, lw=3)[0])
    loglog(4**2, ti, 'o' + ci)

legendComm = legend(reversed(linesComm), reversed(tLabel), loc='upper left')

grid(which='minor')
gca().add_artist(legendComm)
gca().add_artist(legendComp)
xlabel('Spatial points per node $n$')
ylabel('Total time per sub-timestep')
savefig('trend-simplified-2d')

# ---------------------- swept 3d ------------------------- #
figure()

for si in s:
    for ti in t:
        loglog(n, n * si + 6 * ti / n**(1./3), '-', color='#444444')

linesComp = []
for si in s[:3]:
    linesComp.append(loglog(n, n * si, '--', lw=3)[0])
for si in s[3:]:
    linesComp.append(loglog(n, n * si, '-.', lw=3)[0])

legendComp = legend(reversed(linesComp), reversed(sLabel), loc='lower left')

linesComm = []
for ti, ci in zip(t, tColor):
    linesComm.append(loglog(n, 6 * ti / n**(1./3), '-' + ci, lw=3)[0])
    loglog(6**3, ti, 'o' + ci)

legendComm = legend(reversed(linesComm), reversed(tLabel), loc='upper left')

grid(which='minor')
gca().add_artist(legendComm)
gca().add_artist(legendComp)
xlabel('Spatial points per node $n$')
ylabel('Total time per sub-timestep')
savefig('trend-simplified-3d')

