protien_dict ={
    "Methionine":"AUG",
    "Phenylalanine":["UUU","UUC"],
    "Leucine":["UUA","UUG"],
    "Serine":["UCU","UCC","UCA","UCG"],
    "Tyrosine":["UAU","UAC"],
    "Cysteine":["UGU","UGC"],
    "Tryptophan":"UGG",
    "STOP":["UAA","UAG","UGA"]
}

def proteins(strand):
    protien_list = []
    if len(strand) % 3 != 0:
        return "Incomplete RNA Strand Input (not divisible by 3)."
    else:
        codon_list = [strand[i:i+3] for i in range(0,len(strand), 3)]

    for item in codon_list:
        if item in protien_dict["STOP"]:
            return protien_list
        for protien_name,codon in protien_dict.items():
            if item in codon:
                protien_list.append(protien_name)
    return protien_list