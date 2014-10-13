"""
   pyfly2
   
   example_grab_many

   grab many images from the first camera we find and save them to disk
"""

import example_grab
    
if __name__ == "__main__":
    import sys
    import os

    N = 10 if len(sys.argv) <= 1 else int(sys.argv[1])

    for i in xrange(N):
        fname = os.path.join("captures", "Capture%03d.jpg" % i)
        example_grab.grab(fname)