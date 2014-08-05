from optparse import OptionParser
import sys

def main():
    r"""
    DESCRIPTION
    -----------
    Put the description of what the utility does here.

    EXAMPLES
    --------
    Describe example usage here.
    python util.py [options] [file]
    """
    usage = "usage: %prog [options] dataset"
    usage += '\n'+main.__doc__
    parser = OptionParser(usage=usage)
    parser.add_option(
        "-o", "--option1",
        help="Description of the option [default: %default] ",
        action="store", dest='option1', type=float, default=2)

    (options, args) = parser.parse_args()

    ### Parse args
    # Raise an exception if the length of args is greater than 1
    assert len(args) <= 1
    infilename = args[0] if args else None

    ## Get the infile
    if infilename:
        infile = open(infilename, 'r')
    else:
        infile = sys.stdin

    ## Call the function that does the real work
    run(infile, sys.stdout, options)

    ## Close the infile iff not stdin
    if infilename:
        infile.close()

def run(infile, outfile, options):
    """
    Describe what's actually being done
    """
    for linenumber, line in enumerate(infile):
        outfile.write(line)

if __name__=='__main__':
    main()
