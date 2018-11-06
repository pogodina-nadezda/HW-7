class Dna(str):
    def __init__(self, nucleotides):
        self.nucleotides = nucleotides
        
    def gc(self):
        self.GC_content = (self.nucleotides.count('G') + self.nucleotides.count('C')) / len(self.nucleotides) * 100
        return(round((self.GC_content), 2), "%")
        
    def reverse_complement(self):
        self.complement = self.maketrans('ATCG', 'TAGC')
        return(self.nucleotides.translate(self.complement))
        
    def transcribe(self):
        self.complement_RNA = self.maketrans('ATCG', 'UAGC')
        return(self.nucleotides.translate(self.complement_RNA))

class Rna(str):
    def __init__(self, nucleotides):
        self.nucleotides = nucleotides
        
    def gc(self):
        self.GC_content = (self.nucleotides.count('G') + self.nucleotides.count('C')) / len(self.nucleotides) * 100
        return(round((self.GC_content), 2), "%")
        
    def reverse_complement(self):
        self.complement = self.maketrans('AUCG', 'UAGC')
        return(self.nucleotides.translate(self.complement))
