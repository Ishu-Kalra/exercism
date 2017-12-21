t = str.maketrans("GCTA", "CGAU")

def to_rna(dna_strand):
    if any(dna not in "GCTA" for dna in dna_strand):
        raise ValueError("not GCTA")
    return dna_strand.translate(t)
