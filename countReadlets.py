#!/home/bst/student/afrazee/software/Python-2.7.2/python

### TO USE:  countReadlets -f infile.bam -o outfile.txt -k readletlength -c chromosome
### chromosome needs to match the chromosome IDs used in the reference/index used to create the bam file


def enum(collection,st):
    #just like "enumerate" but you define your own starting position.
    #this returns indices RELATIVE TO ORIGINAL LIST
    i = st
    while i < len(collection):
        yield (i,collection[i])
        i += 1

def getfirstindex(L,st,value,K):
    for pos,t in enum(L,st):
        if t[1] > value-K:
            return pos #returns first read in the list that CAN contain given bp
    return 0

def getlastindex(L,st,value):
    for pos,t in enum(L,st):
        if t[1] > value:
            return pos #returns first read in the list that CANNOT contain given bp
    return len(L)

# these 2 were inspired by code here: http://stackoverflow.com/questions/946860/using-pythons-list-index-method-on-a-list-of-tuples-or-objects (see answer labeled "10", superperformant)

def countReadlets(fname,outfname,k,chromosome):
    import pysam
    #from datetime import datetime #for debugging
    samfile = pysam.Samfile(fname,"rb")
    id_start_end = []
    maxpos = 0
    minpos = 3000000000
    for read in samfile.fetch(chromosome):
        id_start_end.append([read.qname, read.pos+1, read.aend])
        if read.aend > maxpos:
            maxpos = read.aend
        if read.pos+1 < minpos:
            minpos = read.pos+1
    f = open(outfname, 'w')
    #g = open('keeptrackofiterations','w') #for debugging
    first = 0
    last = 0
    #npos = 0 #for debugging
    for z in xrange(1,minpos):
        f.write("%s\t%s\n" % (z,0))
    for i in xrange(minpos, maxpos+1):
    #for i in xrange(maxpos-2999,maxpos+1): #for debugging
        #npos = npos+1 #for debugging
        #if npos % 10000 == 0: g.write("Did 10000 "+str(datetime.now())+"\n") #for debugging
        last = getlastindex(id_start_end,first,i)
        first = getfirstindex(id_start_end,first,i,k)
        if first == last:
            f.write("%s\t%s\n" % (i,0))
            continue
        overlaps = id_start_end[first:last]
        readnames = set()
        for j in xrange(len(overlaps)):
            readnames.add(overlaps[j][0])
        numreads = len(readnames) #count readlets only once per read
        f.write("%s\t%s\n" % (i,numreads))
    f.close()
    return None

# get arguments from command line
from optparse import OptionParser
opts = OptionParser()
opts.add_option("--file","-f",type="string",help="input file name (must be .bam)")
opts.add_option("--output","-o",type="string",help="output file name")
opts.add_option("--kmer","-k",type="int",help="kmer length")
opts.add_option("--chrom","-c",type="string",help="chromosome to parse")
options,arguments = opts.parse_args()


countReadlets(options.file,options.output,options.kmer,options.chrom)
