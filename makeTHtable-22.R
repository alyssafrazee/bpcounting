## merge tophat count tables from sarven's data - chr22
## AF 14 Dec 2012

## reads the file "22-bybp" (the output file from countTophatReads.py) for each sample.  Merges these files together for each sample.  Requires lots of memory (~75G for chromosome 22, >300G for chr 1-2)

samps = c("orbFrontalF1","orbFrontalF2","orbFrontalF3","orbFrontalF11","orbFrontalF23","orbFrontalF32","orbFrontalF33","orbFrontalF40",
  "orbFrontalF42", "orbFrontalF43", "orbFrontalF47", "orbFrontalF53", "orbFrontalF55", "orbFrontalF56", "orbFrontalF58",
  "orbFrontalF12", "orbFrontalF19", "orbFrontalF20", "orbFrontalF26", "orbFrontalF27", "orbFrontalF28", "orbFrontalF31",
  "orbFrontalF36", "orbFrontalF48", "orbFrontalF49", "orbFrontalF50", "orbFrontalF51", "orbFrontalF57", "orbFrontalF60")

countlist = list()
for(s in 1:length(samps)){
    print(paste("reading: sample",samps[s]))
      y = read.table(paste("/amber2/scratch/jleek/orbFrontal/results/",samps[s],"/tophat-G/22-bybp",sep=""),sep="\t",header=F)
      print("done reading.")
      countlist[[s]] = y$V2
      if(s==1) pos = y$V1
      if(s>1){
            if(length(y$V1)>length(pos)) pos = y$V1
          }
      rm(y);gc();gc();gc();gc()
  }



lengths = unlist(lapply(countlist,length))
thelen = max(lengths)

for(i in 1:length(countlist)){
    countlist[[i]] = c(countlist[[i]],rep(0,thelen-length(countlist[[i]])))
  }

names(countlist) = samps

chr22.table = as.data.frame(countlist)
chr22.table = data.frame(pos,chr22.table)
write.table(chr22.table, file="/amber2/scratch/jleek/orbFrontal/results/tophat22", row.names=FALSE, quote=FALSE, sep="\t")
