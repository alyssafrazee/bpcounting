#!/bin/sh

# runs counter script for one chromosome
# sh count.sh 21 (e.g.) makes the coverage file for chromosome 21

source k
source args
CHROM=$1

cat >.$CHROM.$SAMPLE.count.sh<<EOF
#run bam file through python counter script 
mkdir -p $SCRATCH_DIR/$SAMPLE
$PYTHON27 $COUNT_SCR -f $SCRATCH_DIR/$SAMPLE.sorted.bam -o $SCRATCH_DIR/$SAMPLE/$CHROM -k $K -c $CHROM

# zip up final output file
gzip $SCRATCH_DIR/$SAMPLE/$CHROM
EOF

qsub -cwd -l cegs -l mf=30G,h_vmem=40G,h_fsize=10G .$CHROM.$SAMPLE.count.sh



