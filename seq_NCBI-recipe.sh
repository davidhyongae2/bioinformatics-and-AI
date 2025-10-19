#entrez api
#source: National Center for Biotechnology Information. (2013). Entrez Direct: E-utilities on the Unix command line. National Center for Biotechnology Information.https://www.ncbi.nlm.nih.gov/books/NBK25501/
./esearch -db nucleotide -query "bacteria[organism] and Antibodies and cds"  | ./efetch -format fasta_cds_na > cds.fasta

#unix command for drug related genes.
grep -w "drug" -A 15 cds.fasta > drug-related.fasta

#download and open alignment viewer.
#source: Larsson, A. (2014). AliView: A fast and lightweight alignment viewer and editor for large datasets. Bioinformatics, 30(22), 3276–3278. https://doi.org/10.1093/bioinformatics/btu531 
./AliView

#follow Aliview tutorial to color and identify.
https://learnmetabarcoding.github.io/LearnMetabarcoding/otu_phylogeny/otu_trees/alignment_viewing.html

#follow tutorial to generate taxonomy with genes. 
