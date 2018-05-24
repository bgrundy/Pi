#!/usr/bin/env python

'''
Binary Clock program using the
Unicorn HD pi hat

Prints a blue border and then the
date in binary format:

           m s
           i e
     m   h n c
   y o   o u o
   e n d u t n
   a t a r e d
   r h y s s s

Author:  Barry J. Grundy
Purpose: Binary clock made using a Pimoroni Unicorn
         Hat HD and a Raspberry Pi or Pi Zero. This
         version is written for the Unicorn Hat HD
         (16x16).
Usage:   There are no options for this initial
         release.
Version: 1.0 - initial 20180518
'''

####################################################
#  Module imports                                  #
####################################################

import numpy
import time
from datetime import datetime

#  First try and import the sim module
#  If the sim module is not available then
#  import the normal unicornhathd module
try:
    from unicorn_hat_sim import unicornhathd
except ImportError:
    import unicornhathd

####################################################
#  Variable declarations                           #
####################################################

width = 12 # define the 'width' of the binary 
           # values (for numpy)

####################################################
#  Function Definitions                            #
####################################################

def main():
    # rotate so the bottom right is the origin rather
    # than the bottom left.
    unicornhathd.clear()
    unicornhathd.rotation(90) # rotate display 90 deg
    # print the border (in blue)
    for x in range(16):
        # First two columns, last two
        # columns, and the first and 
        # last two rows
        if (x < 4) or (x > 11):
            for y in range(16):
            # pass the horizontal pos,
            # vertical pos, then the 
            # amount of red, grn, blue
                unicornhathd.set_pixel(x,y,0,0,255)
        else:
            for y in (0,1,14,15):
                unicornhathd.set_pixel(x,y,0,0,255)
    try:
        while True:
            # get the date values and place them in a tuple
            # so we can access each value serially
            dt = datetime.now().timetuple()
            # Create and empty list to hold binary values
            bins = []
            # convert to $width digit binaries
            # We access the first 6 values in the tuple
            # which include the fields we are interested in
            for field in range(6):
                bins.append(numpy.binary_repr(dt[field],width))
            # and now for each of the binary values stored
            # in bins
            for x in range(len(bins)):
                # set the column number to decrease left to 
                # right as the Unicorn hat is numbered
                col = 10 - x
                # create a character accessible list of each
                # binary number
                binNums = list(bins[x])
                for c in range(len(binNums)):
                    # we want to access the chars in binNums,
                    # but we also need to start at row 2
                    row = c + 2
                    if binNums[c] == '0':
                        unicornhathd.set_pixel(col,row,255,0,0)
                    else:
                        unicornhathd.set_pixel(col,row,0,255,0)
            # display the pixels
            unicornhathd.show()

    except KeyboardInterrupt:
        print("Exiting...")
        unicornhathd.off()

####################################################
#  Main program loop                               #
####################################################

if __name__ == '__main__':
    main()
