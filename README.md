# QuanGene Tools

<p align="center">
    <img src="images/dna.jpg" />
<p>

QuanGene provides generalizable quantitative genetics tools within simple, easy-to-use Python scripts. Each directory contains code for a specific use case, see below for information on each directory. 
# genetic_map 
  * genetic_map.py
    * Purpose: Runs pairwise comparisons between SNPs to calculate recombination frequencies. 
    * Input: XLSX file with the SNP data (SNPs as columns, Lines as rows, see example "BarleyChrom1.xlsx")
    * Output: CSV file containing recombination frequencies for each unique pair of SNPs (see example "recombination_frequency.csv")
