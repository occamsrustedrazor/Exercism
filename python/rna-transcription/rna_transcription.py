def to_rna(dna_strand):
    transcription_dict = {
        "C":"G",
        "G":"C",
        "T":"A",
        "A":"U"
    }
    return ''.join([transcription_dict[i] for i in dna_strand])