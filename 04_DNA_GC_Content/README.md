#DNA GC CONTENT

#BIOLOGICAL BACKGROUND

The percentege of guanines (G) and cytosines (C) in a DNA strand determine
his thermal stability, because this nucleotides are complementary and form
three hydrogen bonds, unlike adenine (A) and thymine (T), wich only form
two. A DNA with a higher GC percentage is more stable and requires a higher
temperature to separate (denature). This is especially important in techniques
such as PCR for melting temperature, designing primers and setting the
annealing temperature to effectively amplify the DNA strand and design
precise genetic experiments.

Also is very important in identication, this beacuse GC percentage is a unique
genetic signature for different species and groups of bacteria, and comparing
these values helps researchers to classify microorganisms and discover new
species, and research and describe adaptation mechanisms; the genomes of
certain organisms develop a higher GC content depending on their enviroment,
so analyzing this ratio, helps us understand the evolutionary pressures
on species.

#Rosalind Problem
The GC-content of a DNA string is given by the percentage of symbols in the string
that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that
the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly
used method of string labeling is called FASTA format. In this format, the string
is introduced by a line that begins with '>', followed by some labeling information.
Subsequent lines contain the string itself; the first line to begin with '>' indicate
the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the
ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

- Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
- Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error below.
