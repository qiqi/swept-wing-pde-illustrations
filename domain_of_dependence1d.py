from pylab import *
from numpy import *

nx = 33
nt = 33
markersize = 5

def prepFigure():
    figure()
    plot(kron(arange(nx), ones(nt)), kron(ones(nx), arange(nt)),
         'o', color='#eeeeee', mec='#eeeeee', markersize=markersize)
    
    axis('scaled')
    xlim([-1/2, nx-1/2])
    ylim([-1/2, nt-1/2])
    xlabel('spatial point')
    ylabel('sub-timestep')

prepFigure()

for t in range(nt // 2 + 1):
    iBegin, iEnd = nx // 2 - t, nx // 2 + t + 1
    plot(arange(iBegin, iEnd), nt//2 + t + zeros(iEnd - iBegin),
         'o', color='#eeeeee', mec='r', markersize=markersize+1)
    plot(arange(iBegin, iEnd), nt//2 - t + zeros(iEnd - iBegin),
         'o', color='b', mec='b', markersize=markersize)

savefig('domainOfDependence')
