from pylab import *
from numpy import *

def plotWithShift(shift, shadow=0):
    nLine = 5
    if not shadow:
        figure()
        axis('scaled')
        axis([-nLine,nLine,-nLine,nLine])
        axis('off')
    
    R = array([[-0.5, sqrt(3) / 2], [-sqrt(3)/2, -0.5]])
    
    x0 = arange(nLine) * 3 - (1.5 - shift) * nLine
    x1 = arange(nLine) * 3 - (1.5 - shift) * nLine
    y0 = zeros(nLine) - 1.5 * nLine
    y1 = zeros(nLine) + 1.5 * nLine
    plot([x0, x1], [y0, y1], ':'*shadow + 'r')
    
    x0, y0 = dot(R, [x0, y0])
    x1, y1 = dot(R, [x1, y1])
    plot([x0, x1], [y0, y1], ':'*shadow + 'g')
    
    x0, y0 = dot(R, [x0, y0])
    x1, y1 = dot(R, [x1, y1])
    plot([x0, x1], [y0, y1], ':'*shadow + 'b')

    if not shadow:
        plotWithShift(shift - 0.1, shadow+1)

s3 = sqrt(3)

# plotWithShift(0.3)
# plot([0], [0], 'ok')

plotWithShift(0.4)
plot([[0, 0, 0], [-1, .5, .5]],
     [[0, 0, 0], [0, s3/2, -s3/2]], '--k', lw=2)
plot([-1, .5, .5, -1],
     [0, s3/2, -s3/2, 0], '-k', lw=3)
savefig('swept2d-illustration-1')

plotWithShift(0.5)
plot([[0, 0, 0], [-2, 1, 1]],
     [[0, 0, 0], [0, s3, -s3]], '--k', lw=2)
plot([-2, 1, 1, -2],
     [0, s3, -s3, 0], '-k', lw=3)
savefig('swept2d-illustration-2')

plotWithShift(0.6)
plot([[0, 0, 0], [-2, 1, 1]],
     [[0, 0, 0], [0, s3, -s3]], '--k', lw=2)
plot([-1.5, 0, 1.5, 1.5, 0, -1.5, -1.5],
     [s3/2, s3, s3/2,
     -s3/2, -s3, -s3/2, s3/2], 'k', lw=3)
plot([[-1.5, 0, 0], [-2, 1, 1], [-1.5, 1.5, 1.5]],
     [[s3/2, s3, -s3], [0, s3, -s3], [-s3/2, s3/2, -s3/2]], 'k', lw=2)
savefig('swept2d-illustration-3')

plotWithShift(0.7)
plot([[0, 0, 0], [-2, 1, 1]],
     [[0, 0, 0], [0, s3, -s3]], '--k', lw=2)
plot([-2, -1, 1, 2, 1, -1, -2],
     [0, s3, s3, 0, -s3, -s3, 0], 'k', lw=2)
plot([2, -1, -1, 2],
     [0, s3, -s3, 0], '-k', lw=3)
savefig('swept2d-illustration-4')

plotWithShift(0.8)
plot([[0, 0, 0], [-2, 1, 1]],
     [[0, 0, 0], [0, s3, -s3]], '--k', lw=2)
plot([[1, -.5, -.5], [2, -1, -1]],
     [[0, s3/2, -s3/2], [0, s3, -s3]], 'k', lw=2)
plot([-2, -1, 1, 2, 1, -1, -2],
     [0, s3, s3, 0, -s3, -s3, 0], 'k', lw=2)
plot([1, -.5, -.5, 1],
     [0, s3/2, -s3/2, 0], '-k', lw=3)
savefig('swept2d-illustration-5')

plotWithShift(0.9)
plot([[0, 0, 0], [-2, 1, 1]],
     [[0, 0, 0], [0, s3, -s3]], '--k', lw=2)
plot([[0, 0, 0], [2, -1, -1]],
     [[0, 0, 0], [0, s3, -s3]], 'k', lw=2)
plot([-2, -1, 1, 2, 1, -1, -2],
     [0, s3, s3, 0, -s3, -s3, 0], 'k', lw=2)
savefig('swept2d-illustration-6')

