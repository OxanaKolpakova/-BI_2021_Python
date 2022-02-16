class my_class(object):

    def __init__(self, seq):
        self.seq = seq

    def translate(self):
        map = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
            "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
            "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
            "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
            "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
            "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
            "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
            "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
            "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
            "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
            "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
            "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
            "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
            "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
            "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
            "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",}
        protein = ''
        for i in range(0,len(self.seq),3):
            test_seq = self.seq[i:i+3]
            protein += map[test_seq]
    return(protein)
  
    def reverse_transcription(self):
        map = {"A":"T", "G":"C", "C":"G", "U":"A",}
        seq = ''
        reverse_seq = self.seq[::-1]
        for i in reverse_seq:
            seq += map[i]
        return(seq)
