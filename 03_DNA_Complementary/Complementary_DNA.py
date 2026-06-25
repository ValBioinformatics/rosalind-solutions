Rules={
    "A":"T",
    "C":"G",
    "G":"C",
    "T":"A",
}

DNA_translate_table= str.maketrans(Rules)
"""A dictionary makes it possible to establish the rules of biological complementarity for DNA
specifying wich nucleotide is assigned to each one"""

def Replication_complementary(dna_sequence: str) ->str:
    return dna_sequence.translate(DNA_translate_table)[::-1]
"""The "Replication_complementary" function carries out the biological process of DNA replication, in wich a template DNA strand
is used to synthesize a new strand by adding each nucleotide acording to the rules of complementarity described"""

def main():
    with open("03_DNA_Complementary/rosalind_revc.txt", "r") as f:
        dna=f.read().strip()
    Complementary_strand=Replication_complementary(dna)
    print(Complementary_strand)

if __name__=="__main__":
    main()
    
    