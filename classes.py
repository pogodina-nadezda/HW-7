class Rna(str):
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        if set(self.sequence) <=  set('ACGTU'):
            pass
        else:
            raise ValueError('Your sequence contains inappropriate nucleotides')

    def gc(self):
        self.GC_content = (self.sequence.count('G') + self.sequence.count('C')) / len(self.sequence) * 100
        return round((self.GC_content), 2)

    def reverse_complement(self):
        self.complement = self.maketrans('AUTCG', 'UAAGC')
        return self.sequence.translate(self.complement)[::-1]

class Dna(Rna):
    def reverse_complement(self):
        self.complement_Dna = self.maketrans('ATCG', 'TAGC')
        return self.sequence.translate(self.complement_Dna)[::-1]

    def transcribe(self):
        return Rna.reverse_complement(self)
