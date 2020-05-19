from sample import Sample

class Drums(Sample):
    def __init__(self, bpm, wav):
        super().__init__(wav)
        self.bpm = bpm
