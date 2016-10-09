import numpy as np

try:
    range = xrange
except NameError:
    pass

def zigzag_pts(steps):
    '''produce zigzag coordinates visiting every integer point in cube with faces parallel to'''
    '''the axes planes with one vertex at the origin and one at steps(which is also the number'''
    '''of steps an axis has)'''
    steps = np.array(steps).astype('int64')

    #number of steps until each axis reverses
    reverse_steps = np.cumprod(steps.astype('int64'))

    pt = np.zeros_like(steps)

    #yield points until the last 
    for cnt in range(reverse_steps[-1]):
        #for each step add +1, 0, or -1. Value is 0 if we are a multiple of a reverse or not a multiple of a previous axis' reverse.
        #add 1 if we're less than halfway through 2 reversals and -1 if more than halfway.
        pt += np.sign([(s - cnt % (2 * s)) * (cnt % s) * (c * cnt % s == 0) for s, c in zip(reverse_steps, steps)])
        yield pt
