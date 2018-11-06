class Rna(str):
    def __init__(self, nucleotides):
        self.nucleotides = nucleotides

    def gc(self):
        self.GC_content = (self.nucleotides.count('G') + self.nucleotides.count('C')) / len(self.nucleotides) * 100
        return round((self.GC_content), 2)

    def reverse_complement(self):
        self.complement = self.maketrans('AUTCG', 'UAAGC')
        return self.nucleotides.translate(self.complement)


class Dna(Rna):
    def reverse_complement(self):
        self.complement_Dna = self.maketrans('ATCG', 'TAGC')
        return self.nucleotides.translate(self.complement_Dna)

    def transcribe(self):
        return Rna.reverse_complement(self)
