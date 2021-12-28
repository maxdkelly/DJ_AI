from lib.elements.sample import Sample

class Bass(Sample):
    def __init__(self, bpm, key, wav):
        super().__init__(wav)
        self.key = key
        self.bpm = bpm
        self.wav = wav