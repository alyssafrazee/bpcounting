bpcounting
==========

code for getting per-bp coverage from read alignment files

FILE IN HERE:

countReadlets.py:  python script taking a bam file of readlet alignments (from bowtie, with readlets from same 
read having the same ID up to the first whitespace character) and outputting a 2-column matrix (col 1: position, 
col 2: coverage at read level - i.e., readlets from same read are only counted as 1).  Matrix is written to disk 
as a text file.

count
