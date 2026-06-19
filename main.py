codon_table = {
    "ATG": "Methionine",
    "TTT": "Phenylalanine",
    "TTC": "Phenylalanine",
    "GAA": "Glutamic Acid",
    "GAG": "Glutamic Acid",
    "TAA": "STOP",
    "TAG": "STOP",
    "TGA": "STOP"
}

dna = input("Enter DNA sequence: ").upper().replace(" ", "")

valid_bases = {"A", "T", "G", "C"}

for base in dna:
    if base not in valid_bases:
        print("Invalid DNA sequence. Only A, T, G, C allowed.")
        exit()

codons = [dna[i:i+3] for i in range(0, len(dna), 3)]

protein_chain = []

print("\nCodons:", codons)
print("\nTranslation:")

for codon in codons:
    if len(codon) < 3:
        continue

    amino_acid = codon_table.get(codon, "Unknown")

    print(codon, "->", amino_acid)

    if amino_acid == "STOP":
        break

    if amino_acid != "Unknown":
        protein_chain.append(amino_acid)

print("\nProtein Chain:")
print(" - ".join(protein_chain))
