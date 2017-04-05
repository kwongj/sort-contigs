#!/usr/bin/env python
# Script by JK
# Sort contigs in GBK or FASTA file

# Use modern print function from python 3.x
from __future__ import print_function

# Import modules
import argparse
import os
import sys
import StringIO
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# Usage
parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description='Sort contigs in a GBK or FASTA file',
		usage='\n  %(prog)s [--order order.txt] CONTIGS.GBK | CONTIGS.FA')
parser.add_argument('contigs', metavar='FILE', nargs=1, help='genbank or FASTA file to sort')
parser.add_argument('--fmt', metavar='FORMAT', nargs=1, required=True, help='file format (fasta|genbank)')
parser.add_argument('--order', metavar='FILE', nargs=1, help='specified order (list of contigs must match contig names)')
parser.add_argument('--out', metavar='FILE', nargs=1, help='Output file (optional - otherwise will print to stdout)')
parser.add_argument('--version', action='version', version='%(prog)s version 1.0\nUpdated 23-Nov-2016\nScript by JK')
args = parser.parse_args()

ctgfile = args.contigs[0]
format = args.fmt[0]
if args.order:
	orderfile = args.order[0]
if args.out:
	outfile = args.out[0]

# Functions
# Log a message to stderr
def msg(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

# Log an error to stderr and quit with non-zero error code
def err(*args, **kwargs):
	msg(*args, **kwargs)
	sys.exit(1);

# Check file exists
def check_file(f):
	if os.path.isfile(f) == True:
		err('ERROR: Output file "{}" already exists. Please specify a new output file.'.format(f))

# Parse contigs
ctglist = {}
ctg_ids = []
seqNEW = []
for seqREC in SeqIO.parse(ctgfile, format):
	ctglist[seqREC.id] = seqREC
	ctg_ids.append(seqREC.id)
if len(ctg_ids) < 1:
	err('ERROR: Check file format.')
if args.order:
	with open(orderfile) as file:
		ctg_ids = [line.rstrip() for line in file]
else:
	ctg_ids.sort()
for id in ctg_ids:
	seqNEW.append(ctglist[id])

# Write new ordered file or print to stdout
if args.out:
	check_file(outfile)
	msg('Sorted contigs saved to "{}" ... '.format(outfile))
	SeqIO.write(seqNEW, outfile, format)
else:
	seqFILE = StringIO.StringIO()
	SeqIO.write(seqNEW, seqFILE, format)
	output = seqFILE.getvalue().rstrip()
	print(output)

sys.exit(0)
