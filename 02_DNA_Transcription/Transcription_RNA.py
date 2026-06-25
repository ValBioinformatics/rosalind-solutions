def transcribe_dna_to_rna(dna_sequence: str) ->str:
    return dna_sequence.replace ("T", "U")
"""Converts a DNA string in to a RNA transcript, replaces each thymine (T) with Uracile (U)
#Args: dna_sequence: a string of DNA nucleotides (A, T, C, G)
#Returns: RNA string with T replaced with by U"""

def main():
    with open("rosalind_rna.txt", "r") as f:
        dna=f.read().strip()
    rna=transcribe_dna_to_rna(dna)
    print (rna)

if __name__=="__main__":
    main()
    





