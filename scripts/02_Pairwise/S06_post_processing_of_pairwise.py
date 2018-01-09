#!/usr/bin/env python
## AUTHOR: Eric Fontanillas
## LAST VERSION: 14/08/14 by Julie BAFFARD

MINIMUM_LENGTH = 1

#######################
##### RUN RUN RUN #####
#######################
import string, os, time, re, sys
from functions import get_pairs, extract_length, filter_redondancy

## 1 ## INPUT/OUTPUT
SHORT_FILE = sys.argv[1] #short-name-query_short-name-db

F_IN = "%s/06_PairwiseMatch_%s.fasta" %(SHORT_FILE, SHORT_FILE) 

F_OUT = "%s/09_PairwiseMatch_filtered_%s.fasta" %(SHORT_FILE, SHORT_FILE) 
File_OUT = open(F_OUT, "w")

F_OUT2 = "%s/09_onlyMatch_filtered_%s.fasta" %(SHORT_FILE, SHORT_FILE) 
File_OUT2 = open(F_OUT2, "w")

## 2 ## RUN
list_pairwises = get_pairs(F_IN)           ### DEF1 ###
list_pairwises_filtered1 = filter_redondancy(list_pairwises, MINIMUM_LENGTH)                ### DEF3 ###

i = 0
for pair in list_pairwises_filtered1:
     i = i+1

     ## Write pairwise alignment
     File_OUT.write("%s\n" %pair[0])
     File_OUT.write("%s\n" %pair[1])
     File_OUT.write("%s\n" %pair[2])
     File_OUT.write("%s\n" %pair[3])

     ## Write only "matches" [AND UNGAP THEM: needed before the 2nd run of blast]
     File_OUT2.write("%s\n" %pair[2])
     seq_match = pair[3]
     seq_match_ungapped = string.replace(seq_match, "-", "")
     File_OUT2.write("%s\n" %seq_match_ungapped)
    
File_OUT.close()
File_OUT2.close()
