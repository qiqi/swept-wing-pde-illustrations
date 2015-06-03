import os
from string import Template
from subprocess import call
from numpy import linspace

for eType in ['upPyramid', 'bridge', 'pavement']:
    template = Template(open('{0}.pov'.format(eType)).read())
    for i, t in enumerate(linspace(0,1,121)[:-1]):
        if not os.path.exists('{0}{1:03d}.png'.format(eType, i)):
            fname = '{0}{1:03d}.pov'.format(eType, i)
            with open(fname, 'w') as f:
                f.write(template.substitute(t=t))
            call(['povray', '-D', '+H1080', '+W1920', fname])
            call(['rm', fname])
    call(['avconv', '-i', r'{0}%3d.png'.format(eType), '-r', '30',
          '-b:v', '8M', '-vcodec', 'h264', '{0}.avi'.format(eType)])
