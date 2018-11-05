class Dna(str):
    def __init__(self, nucleotides):
        self.nucleotides = nucleotides
        
    def gc(self):
        self.GC_content = (self.nucleotides.count('G') + self.nucleotides.count('C')) / len(self.nucleotides) * 100
        print(round((self.GC_content), 2), "%")
        
    def reverse_complement(self):
        self.complement = self.maketrans('ATCG', 'TAGC')
        print(self.nucleotides.translate(self.complement))
        
    def transcribe(self):
        self.complement_RNA = self.maketrans('ATCG', 'UAGC')
        print(self.nucleotides.translate(self.complement_RNA))

class Rna(str):
    def __init__(self, nucleotides):
        self.nucleotides = nucleotides
        
    def gc(self):
        self.GC_content = (self.nucleotides.count('G') + self.nucleotides.count('C')) / len(self.nucleotides) * 100
        print(round((self.GC_content), 2), "%")
        
    def reverse_complement(self):
        self.complement = self.maketrans('AUCG', 'UAGC')
        print(self.nucleotides.translate(self.complement))
