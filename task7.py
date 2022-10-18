from abc import ABC, abstractmethod
import random

class NA(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __getitem__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __mul__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def reverse(self):
        pass

    @abstractmethod
    def complement(self):
        pass

    def reverse_complement(self):
        return self.reverse().complement()

class DNA(NA):

    def __init__(self, seq: str):
        if not set(seq.upper()).issubset(set('ATGC')):
            raise Exception("Wrong sequence! Sequence must only consist of 'A', 'T', 'G' and 'C'")

        self.coding_seq = seq.upper()
        self.matrix_seq = self.coding_seq.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper() #use of lowercase letter - it's genius!
        self.length = len(seq)

    def __getitem__(self, i):
        return {'coding': self.coding_seq[i], 'matrix': self.matrix_seq[i]}

    def __str__(self):
        return f'coding: {self.coding_seq}, matrix: {self.matrix_seq}\nlength = {self.length}'

    def __repr__(self):
        if self.length > 50:
            return f'coding: {self.coding_seq[:25]}...{self.coding_seq[-25:]}, matrix: {self.matrix_seq[:25]}...{self.coding_seq[-25:]}\nlength = {self.length}, type=DNA'
        else:
            return f'coding: {self.coding_seq}, matrix: {self.matrix_seq}\nlength = {self.length}, type=DNA'

    def __add__(self, other):
        if not isinstance(other, DNA):
            raise TypeError('Unsupported type!')

        return DNA(self.coding_seq + other.coding_seq)

    def __mul__(self, other):
        if not isinstance(other, DNA):
            raise TypeError('Unsupported type!')

        coding_seq = ''
        if self.length < other.length:
            for i in range(self.length):
                coding_seq += random.choice([self.coding_seq[i], other.coding_seq[i]])
            coding_seq += other.coding_seq[self.length:]

        else:
            for i in range(other.length):
                coding_seq += random.choice([self.coding_seq[i], other.coding_seq[i]])
            coding_seq += other.coding_seq[other.length:]

        return DNA(coding_seq)

    def __eq__(self, other):

        if isinstance(other, DNA):
            return self.coding_seq == other.coding_seq

        elif isinstance(other, RNA):
            return self.coding_seq.replace('T', 'U') == other.seq

        else:
            raise TypeError('Unsupported type!')

    def transcription(self):
        return RNA(self.coding_seq.replace('A', 'u').replace('T', 'a').replace('G', 'c').replace('C', 'G').upper())

    def complement(self):
        return DNA(self.matrix_seq)

    def reverse(self):
        return DNA(self.coding_seq[::-1])


class RNA(NA):

    def __init__(self, seq: str):
        if not set(seq.upper()).issubset(set('AUGC')):
            raise Exception("Wrong sequence! Sequence must only consist of 'A', 'U', 'G' and 'C'")

        self.coding_seq = seq.upper()
        self.length = len(seq)

    def __getitem__(self, i):
        return self.coding_seq[i]

    def __str__(self):
        return f'{self.coding_seq}\nlength = {self.length}'

    def __repr__(self):
        if self.length > 50:
            return f'{self.coding_seq[:25]}...{self.coding_seq[-25:]}\nlength = {self.length}, type=RNA'
        else:
            return f'{self.coding_seq}\nlength = {self.length}, type=RNA'

    def __add__(self, other):
        if not isinstance(other, RNA):
            raise TypeError('Unsupported type!')

        return RNA(self.coding_seq + other.coding_seq)

    def __mul__(self, other):
        if not isinstance(other, RNA):
            raise TypeError('Unsupported type!')

        coding_seq = ''
        if self.length < other.length:
            for i in range(self.length):
                coding_seq += random.choice([self.coding_seq[i], other.coding_seq[i]])
            coding_seq += other.coding_seq[self.length:]

        else:
            for i in range(other.length):
                coding_seq += random.choice([self.coding_seq[i], other.coding_seq[i]])
            coding_seq += other.coding_seq[other.length:]

        return RNA(coding_seq)

    def __eq__(self, other):

        if isinstance(other, RNA):
            return self.coding_seq == other.coding_seq

        elif isinstance(other, DNA):
            return self.coding_seq.replace('U', 'T') == other.seq

        else:
            raise TypeError('Unsupported type!')

    def reverse_transcription(self):
        return DNA(self.coding_seq.replace('A', 't').replace('U', 'a').replace('G', 'c').replace('C', 'g').upper())

    def complement(self):
        return RNA(self.coding_seq.replace('A', 'u').replace('U', 'a').replace('G', 'c').replace('C', 'g').upper())

    def reverse(self):
        return RNA(self.coding_seq[::-1])


x = RNA('augcaucgauuuugcgcgcaua')
print(x)
print(x.reverse_complement())