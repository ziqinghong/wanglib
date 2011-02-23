"""This file provides useful utilities for the wanglib package."""

import serial
from time import sleep

class Serial(serial.Serial):
    """ Extension of the standard serial class.  """
    
    def readall(self):
        """Automatically read all the bytes from the serial port."""
        return self.read(self.inWaiting())

    def ask(self, query, lag=0.05):
        """
        Write to the bus, then read response.

        This doesn't seem to work very well.

        """
        self.write(query)
        sleep(lag)
        return self.readall()

class InstrumentError(Exception):
    """Raise this when talking to instruments fails."""
    pass


def scan_gen(wls, spec, lockin, avgs=1):
    """
    Generator for a scanned spectrum.

    Arguments:
        wls -- list or numpy array containing
                the spectral values to scan over.
        spec -- a spectrometer instance. 
        lockin -- a lockin instance. 

    Keyword Arguments:
        avgs -- the number of data points to average on 
                each spectral value.

    """
#    if lockin is None:
#        lockin = egg5110()
#    if spec is None:
#        spec = triax()

    timeconst, unit = lockin.timeconst
    if unit == "ms":
        timeconst /= 1000.
    elif unit == "s":
        pass
    else:
        raise Exception( "Unknown time unit: %s" % unit)
    for i in range(len(wls)):
        spec.wl = wls[i]
        tally = 0.
        for j in range(avgs):
            sleep(timeconst * 1.2)
            tally += lockin.r[0] # discard unit
        yield tally / avgs


