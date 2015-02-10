from pylab import *
from numpy import *

nx = 16
nt = 24
markersize = 5
nodeColor = ['b', 'r', 'g']
nNode = len(nodeColor)

def prepFigure():
    figure()
    plot(kron(arange(nx * nNode), ones(nt)), kron(ones(nx * nNode), arange(nt)),
         'o', color='#eeeeee', mec='#eeeeee', markersize=markersize)
    
    axis('scaled')
    xlim([-1/2, nx * nNode-1/2])
    ylim([-1/2, nt-1/2])
    xlabel('spatial point')
    ylabel('sub-timestep')

def initialization():
    prepFigure()
    
    for iNode in range(nNode):
        c = nodeColor[iNode]
        iBegin, iEnd = iNode * nx, iNode * nx + nx
        plot(arange(iBegin, iEnd), zeros(iEnd - iBegin),
             'o', color=c, mec=c, markersize=markersize)

def communication(deltaX, deltaT):
    prepFigure()
    
    # ghost nodes
    for iNode in range(nNode):
        c = nodeColor[iNode]
        for t in range(int(nx / 2)):
            if deltaX % nx == 0:
                iBegin = ((iNode + 1) * nx + t) % (nNode * nx) + deltaX
                iEnd = iBegin + 2
            else:
                iEnd = iNode * nx + nx - t + deltaX
                iBegin = iEnd - 2
            plot(arange(iBegin, iEnd), deltaT + t + zeros(2),
                 'o', color='w', mec=c, markersize=markersize + 1, mew=1)
            if deltaX > 0:
                iBegin -= nx * nNode
                iEnd -= nx * nNode
                plot(arange(iBegin, iEnd), deltaT + t + zeros(2),
                     'o', color='w', mec=c, markersize=markersize + 1, mew=1)
            elif deltaX < 0:
                iBegin += nx * nNode
                iEnd += nx * nNode
                plot(arange(iBegin, iEnd), deltaT + t + zeros(2),
                     'o', color='w', mec=c, markersize=markersize + 1, mew=1)
    
    for iNode in range(nNode):
        c = nodeColor[iNode]
        for t in range(int(nx / 2)):
            if deltaX % nx == 0:
                iEnd = iNode * nx + nx - t + deltaX
                iBegin = iEnd - 2
            else:
                iBegin = ((iNode + 1) * nx + t) % (nNode * nx) + deltaX
                iEnd = iBegin + 2
            plot(arange(iBegin, iEnd), deltaT + t + zeros(2),
                 'o', color=c, mec=c, markersize=markersize)
            if deltaX > 0:
                iBegin -= nx * nNode
                iEnd -= nx * nNode
                plot(arange(iBegin, iEnd), deltaT + t + zeros(2),
                     'o', color=c, mec=c, markersize=markersize)
            elif deltaX < 0:
                iBegin += nx * nNode
                iEnd += nx * nNode
                plot(arange(iBegin, iEnd), deltaT + t + zeros(2),
                     'o', color=c, mec=c, markersize=markersize)

def diamond(deltaX, deltaT):
    prepFigure()

    for iNode in range(nNode):
        c = nodeColor[iNode]
        for t in range(int(nx / 2)):
            iBegin, iEnd = deltaX + iNode * nx + t, deltaX + iNode * nx + nx - t

            plot(arange(iBegin, iEnd), deltaT + t + zeros(iEnd - iBegin),
                 'o', color=c, mec=c, markersize=markersize)
            plot(arange(iBegin, iEnd), deltaT - t + zeros(iEnd - iBegin),
                 'o', color=c, mec=c, markersize=markersize)

            plot(arange(iBegin, iEnd) - nx * nNode,
                 deltaT + t + zeros(iEnd - iBegin),
                 'o', color=c, mec=c, markersize=markersize)
            plot(arange(iBegin, iEnd) - nx * nNode,
                 deltaT - t + zeros(iEnd - iBegin),
                 'o', color=c, mec=c, markersize=markersize)

initialization()
savefig('swept1d-illustrate-1')
diamond(0, 0)
savefig('swept1d-illustrate-2')
communication(0, 0)
savefig('swept1d-illustrate-3')
diamond(nx//2, nx//2)
savefig('swept1d-illustrate-4')
communication(-nx//2, nx//2)
savefig('swept1d-illustrate-5')
diamond(0, nx)
savefig('swept1d-illustrate-6')
communication(0, nx)
savefig('swept1d-illustrate-7')
diamond(nx//2, nx*3//2)
savefig('swept1d-illustrate-8')

