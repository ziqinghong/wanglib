#
# This file is a placeholder which makes Python
# recognize this folder as an importable package.
#
# tkb

"""
Experimental control utilities for the Wang lab.

When writing a script to control your experiment (or working interactively
using the interpreter), use wanglib to make instrument control and data
gathering easy.

The core contains these modules:
    
    util -- configures the gpib interface (if any): pyVisa or linux-gpib
            implements a custom serial implementation
            does some strange data fitting / calibration stuff.
    prologix -- drivers for prologix GPIB controllers (USB and Ethernet)
    Gpib -- the linux-gpib python wrapper, modified to use new style classes.
    ccd --  a client for the CCD on the spex750m
    grating -- generates phase gratings for the SLM

more functionality in two sub-packages:

    instruments -- libraries for individual instruments in the lab
    pylab_extensions -- misc. extensions to the pylab plotting interface

This is a code library - not a set of specific experimental routines.  
The script you write to control your experiment will call functions in
wanglib, but should only be a part of wanglib if it is modular, reusable, and
adds functionality not already here.

I welcome contributions and modifications. 

tkb

"""
