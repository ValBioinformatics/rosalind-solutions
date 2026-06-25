# RNA Transcription — Rosalind Problem

## Biological Background

Transcription is the first step of gene expression, in which a DNA 
template is used to synthesize a complementary RNA strand. This process 
is carried out by RNA polymerase, which reads the DNA strand and builds 
the corresponding RNA molecule.

Chemically, RNA differs from DNA in two main ways: RNA uses ribose 
instead of deoxyribose as its sugar backbone, and uracil (U) instead of 
thymine (T) as one of its four nitrogenous bases. At the sequence level, 
this means that transcribing a DNA strand into RNA only requires 
replacing every T with a U; the rest of the sequence remains unchanged.

This simple substitution reflects a deep biological mechanism: it is 
the basis for how genetic information flows from DNA to RNA to protein 
(the central dogma of molecular biology), and it is one of the most 
fundamental sequence transformations in bioinformatics pipelines.

## Problem Statement

Given a DNA string of length at most 1000 nucleotides, return the 
transcribed RNA string by replacing every occurrence of T with U.

## Approach

DNA and RNA differ by a single nucleotide substitution: thymine (T) is 
replaced by uracil (U). All other bases (A, C, G) remain unchanged. 
Since this is a direct character-level substitution, a single string 
replacement operation across the sequence is sufficient.
