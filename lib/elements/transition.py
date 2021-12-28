from lib.elements.sample import Sample

class Transition(Sample):
    def __init__(self, start_bpm, end_bpm, wav):
        super().__init__(wav)
        self.start_bpm = start_bpm
        self.end_bpm = end_bpm
        