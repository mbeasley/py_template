import argparse
import fileinput
import sys

def main():
    epilog = r"""
    """

    parser = argparse.ArgumentParser(
        description=globals()['__doc__'], epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        'infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
        help='process this file or read from stdin')
    parser.add_argument(
        '-o', '--out', default=sys.stdout, type=argparse.FileType('w'),
        help='write to this file rather than sys.stdout')

    args = parser.parse_args()

    ## Call the function that does the real work
    run(args.out, args)

    ## Close the infile iff not stdin
    fileinput.close()

def run(outfile, args):
    """
    Describe what's actually being done
    """
    for line in fileinput.input():
        outfile.write(line)

if __name__=='__main__':
    main()
