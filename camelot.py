import random

class Camelot():

    def __init__(self):

        self.graph = { "A" : ["F#m", "D", "E"],
          "D" : ["A", "G", "Bm"],
          "G" : ["D", "C", "Em"],
          "C" : ["G", "F", "Am"],
          "F" : ["C", "Bb", "Dm"],
          "Bb" : ["F", "Eb", "Gm"],
          "Eb" : ["Bb", "Ab", "Cm"],
          "Ab" : ["Eb", "Db", "Fm"],
          "Db" : ["Ab", "F#", "Bbm"],
          "F#" : ["Db", "B", "Ebm"],
          "B" :  ["F#", "E", "Abm"],
          "E" : ["B", "A", "Dbm"],
          "F#m" : ["Dbm", "Bm", "A"],
          "Bm" : ["F#m", "Em", "D"],
          "Em" : ["Bm", "Am", "G"],
          "Am" : ["Em", "Dm", "C"],
          "Dm" : ["Am", "Gm", "F"],
          "Gm" : ["Dm", "Cm", "Eb"],
          "Cm" : ["Gm", "Fm", "Eb"],
          "Fm" : ["Cm", "Bbm", "Ab"],
          "Bbm" : ["Fm", "Ebm", "Db"],
          "Ebm" : ["Bbm", "Abm", "F#"],
          "Abm" : ["Ebm", "Dbm", "B"],
          "Dbm" : ["Abm", "F#m", "E"],
        }

    def find_samples(self,start_sample, sample_list):

      samples = []
      for node in self.graph:
        if start_sample.key == node:
          for neighbour in self.graph[node]:
            samples = samples + self.find_sample(start_sample.bpm,neighbour,sample_list)

      if not samples:
        return -1

      return sample_list.index(random.choice(samples))

    def find_sample(self,bpm,key,music_list):

      selected_list = []

      for node in music_list:

        if node.key == key and node.bpm == bpm:
          selected_list.append(node)

      return selected_list

            
          
          
