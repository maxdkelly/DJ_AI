from lib.elements.sample import Sample

class Vocal(Sample):
    def __init__(self, bpm, key, wav):
        super().__init__(wav)
        self.bpm = bpm
        self.key = key
        self.wav = wav