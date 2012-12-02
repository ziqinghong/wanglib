#!/usr/bin/env python

from matplotlib.pyplot import gca

def density_plot(two_dimensional, horiz, vert, ax=None):
    """
    Display a 2D density plot - like imshow, but with 
    axes labels corresponding to the two axes provided.

    This will only be accurate for regularly-spaced
    x and y axes (e.g., as generated by arange or linspace).

    :param two_dimensional: data to plot. shape: (M, N)
    :param horiz: x-axis. should have length N.
    :param vert: y-axis. should have length M.
    :param ax: axis upon which to plot.

    """
    if ax is None:
        ax = gca()
    horiz_spacing = (horiz[-1] - horiz[0]) / (len(horiz) - 1.)
    vert_spacing = (vert[-1] - vert[0]) / (len(vert) - 1.)
    # add spacing to the upper bounds. This aligns tick
    # marks with the lower left of pixels
    ext = [horiz[0], horiz[-1] + horiz_spacing,
           vert[0], vert[-1] + vert_spacing]
    # this provides axes labels. Unfortunately it also changes
    # the aspect ratio, so we need to stretch it back.
    asp = (ext[1] - ext[0]) / (ext[3] - ext[2])
    asp /=  float(len(horiz))/ len(vert)
    # the first step alone gets us back to a square image aspect.
    # the second will restore the native aspect ratio of the array.
    ax.imshow(two_dimensional, extent=ext, aspect = asp,
              origin='lower', interpolation='nearest')


