#!/usr/bin/env python
import sys
import struct

def usage():
    print """
    Usage:
        shutter.py path_to_canon_raw_file
    """
    exit(1)
                
def main():
    if len(sys.argv) != 2:
        usage()

    rawfile = sys.argv[1]

    print "Camera Model: ", decode_model(rawfile)
    print "Total shutter counts: ", canon_20D(rawfile)


def decode_model(rawfile):
    with open(rawfile, "rb") as ifh:
        # This appears Canon 20D only
        ifh.seek(0xCA)
        bytes = ifh.read(14)
        return bytes

def canon_20D(rawfile):
    with open(rawfile, "rb") as ifh:
        ifh.seek(0x95D)
        bytes = ifh.read(2)
        ## assuming this is unsigned int ( 2 bytes)
        ## @ for native byte order, < little endian, > for big endian
        res =  struct.unpack(">H", bytes)
        return res[0]

if __name__ == "__main__":
    main()
