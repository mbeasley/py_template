py_template
===========

A template for Python CLI utlities

This is almost an exact copy of the proposed CLI template presented
in [Columbia's applied data science manual](http://columbia-applied-data-science.github.io/appdatasci.pdf),
in chapter 3.2. I use it as a starter template for general purpose file processing scripts.

It is intended to be run via `python util.py [options] [file]`.  By default, the output is printed to `STDOUT`
and the input can be either a file, or if non is supplied, a pipe from `STDIN`: `cat file.csv | python util.py ...`.
