import matplotlib
matplotlib.use('agg')

from pylab import *
from matplotlib import patches
from numpy import *

c = ['r', 'g', 'b', 'c', 'y', 'm'] * 1000
ci = 0
nNodes, nProcs, nCores = 2, 12, 4

iBatch, iPlot = 0, 0

axis('scaled')
xlim([0, (nProcs + nCores) * nNodes])
ylim([0, (nProcs + nCores) * nNodes])
gca().xaxis.set_ticks([])
gca().yaxis.set_ticks([])

for iLevel in range(nProcs - nCores + 1):
    for iNode in range(-1,nNodes):
        for iProc in range(nProcs - iLevel):
            x = iNode * (nProcs + nCores) + iProc + 0.5 * iLevel + array([0, 0.5, 1, 0.5])
            y = 0.5 * iLevel + array([0, -0.5, 0, 0.5])
            y = minimum(maximum(y, 0), 0.5 * (nProcs - nCores))
            gca().add_patch(patches.Polygon(transpose([x, y]), color=c[ci]))
    ci += 1
    savefig('swept1d_2lvl_{0:d}_{1:d}'.format(iBatch, iPlot))
    iPlot += 1

iBatch += 1
iPlot = 0

xShift, yShift = nProcs - 0.5 * nCores, 0
while yShift <= (nProcs + nCores) * nNodes:
    for iLevel in range(nCores, nProcs):
        for iNode in range(-1,nNodes):
            for iProc in range(iLevel):
                x = iNode * (nProcs + nCores) + iProc + xShift + nCores \
                  - 0.5 * iLevel + array([0, 0.5, 1, 0.5])
                y = 0.5 * (iLevel - nCores) + yShift + array([0, -0.5, 0, 0.5])
                y = minimum(maximum(y, yShift), (nProcs - nCores) + yShift)
                gca().add_patch(patches.Polygon(transpose([x, y]), color=c[ci]))
        ci += 1
        savefig('swept1d_2lvl_{0:d}_{1:d}'.format(iBatch, iPlot))
        iPlot += 1
    
    for iLevel in range(nProcs - nCores + 1):
        for iNode in range(-1,nNodes):
            for iProc in range(nProcs - iLevel):
                x = iNode * (nProcs + nCores) + iProc + xShift \
                  + 0.5 * (iLevel - nProcs) + nCores + array([0, 0.5, 1, 0.5])
                y = 0.5 * (nProcs - nCores + iLevel) + yShift + array([0, -0.5, 0, 0.5])
                y = minimum(maximum(y, yShift), (nProcs - nCores) + yShift)
                gca().add_patch(patches.Polygon(transpose([x, y]), color=c[ci]))
        ci += 1
        savefig('swept1d_2lvl_{0:d}_{1:d}'.format(iBatch, iPlot))
        iPlot += 1

    yShift += (nProcs - nCores) * 0.5
    if xShift == 0.5 * nCores:
        xShift = nProcs - 0.5 * nCores
    else:
        xShift = 0.5 * nCores

    print yShift
    iBatch += 1
    iPlot = 0
