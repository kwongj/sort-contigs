# sort-contigs
Sorts contigs in GENBANK or FASTA file

##Author

Jason Kwong (@kwongjc)

##Dependencies
* Python 2.7.x
* BioPython

##Usage

```
$ sort-contigs.py -h
usage: 
  sort-contigs.py [--order order.txt] CONTIGS.GBK | CONTIGS.FA

Sort contigs in a GBK or FASTA file

positional arguments:
  FILE          genbank or FASTA file to sort

optional arguments:
  -h, --help    show this help message and exit
  --fmt FORMAT  file format (fasta|genbank)
  --order FILE  specified order (list of contigs must match contig names)
  --out FILE    Output file (optional - otherwise will print to stdout)
  --version     show program's version number and exit
```

##Bugs

Please submit via the [GitHub issues page](https://github.com/kwongj/sort-contigs/issues).  

##Software Licence

[GPLv3](https://github.com/kwongj/sort-contigs/blob/master/LICENSE)
