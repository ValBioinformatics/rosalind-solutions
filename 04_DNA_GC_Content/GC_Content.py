def calculate_GC(DNA_sequence: str) -> float:
    gc_conteo=DNA_sequence.count("G")+ DNA_sequence.count("C")
    return (gc_conteo/len(DNA_sequence))*100
"""The first Function: Calculate the % of "G" and "C" in a sequence, and returns a decimal number"""

def sequences(Archive:str):
    strands= {}
    Id_actual=""
    """The principal function: Create a dictionary to separate each of the sequences from 
    the FASTA file (Strands) and a empty text variable for the ID of the sequences"""

    with open("04_DNA_GC_Content/rosalind_gc.txt","r") as f:
        for linea in f:
            linea=linea.strip()
            if not linea:
                continue
            """In the FASTA file, read line by line and remove line breaks"""
            if linea.startswith(">"):
                Id_actual=linea[1:]
                strands[Id_actual]=[]
            else:
                strands[Id_actual].append(linea)
            """To identify the ID of each sequence, create a condicional for the sign ">",
            save the ID in "Id_actual", remove the sign >, and add it to the dicionary "strands" 
            to save the sequence."""
                
    for id_seq in strands:
        strands[id_seq]="".join(strands[id_seq])
        """Form one sequence for each ID, each element in the list is a nucleotide of the sequence"""
    mejor_id=""
    max_gc=-1.0
    for id_seq, strand in strands.items():
        actual_percentage=calculate_GC(strand)
        if actual_percentage > max_gc:
            max_gc=actual_percentage
            mejor_id=id_seq
        """Define variables, (mejor id and max gc) and search in the dictionary, sequence by sequence, 
        calculating the percentage of each one using the previous function, and calculating 
        wich percentage is the highest"""
            
    print (mejor_id)
    print (f"{max_gc:.6f}")
    """For Rosalind format"""

if __name__=="__main__":
        sequences("rosalind_gc.txt")
