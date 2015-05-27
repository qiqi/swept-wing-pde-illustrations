from string import Template
from subprocess import call
from numpy import linspace

for eType in ['upPyramid', 'bridge', 'pavement']:
    template = Template(file('{0}.pov'.format(eType)).read())
    for i, t in enumerate(linspace(0,1,120)[:-1]):
        fname = '{0}{1:03d}.pov'.format(eType, i)
        with open(fname, 'w') as f:
            f.write(template.substitute(t=t))
        call(['povray', fname])
        call(['rm', fname])
