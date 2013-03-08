bpcounting
==========

code for getting per-bp coverage from read alignment files

FILE IN HERE:

countReadlets.py:  python script taking a bam file of readlet alignments (from bowtie, with readlets from same read having the same ID up to the first whitespace character) and outputting a 2-column matrix (col 1: position, col 2: coverage at read level - i.e., readlets from same read are only counted as 1).  Matrix is written to disk as a text file.  Input bam file MUST be sorted (can do this using samtools sort).
USAGE:  python countReadlets.py -f infile.bam -o outfile.txt -k readletlength -c chromosome
chromosome must match chromosome IDs used in the index/reference that was used in creating infile.bam.

countTophatReads.py:  same idea as countReadlets.py, but instead of taking a readlet alignment file, takes thetophat output file "accepted_hits.bam".  Tophat sorts this by default.  Accounts for spliced/gapped alignments.
USAGE:  python countTophatReads.py -f accepted_hits.bam -o outfile.txt -k readlength -c chromosome

makeTHtable-22.R:  R script I used to merge all the pos x coverage matrices from the different samples for one chromosome of brain data.  This is the best merge code I have right now (March 8, 2013).  It's horribly inefficient  with memory, but does the job.

bam-to-linear-model.R:  my very very first attempt at writing R code that operates directly on the bam files to get coverage, filter out bps with low coverage, and fit linear models on the remaining bps.  This is NOT finished and is reeeeaaaaaalllllllllyyyyyyyyyyyyy slow.  I mean really slow.  It's not usable.  But it's what I did.  For reference.

