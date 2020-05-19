import random
import time

class Routine():

    def __init__(self, bpm, controller):

        self.bpm = bpm
        self.controller = controller

        self.drum_full_index = self.find_index(None, self.controller.drums_full)
        self.drum_full_index_2 = self.find_index(None, self.controller.drums_full)
        self.drum_tops_index = self.find_index(None, self.controller.drums_tops)
        self.synth_index = self.find_index(None, self.controller.synth_loops)
        self.synth_index_2 = self.find_index(None, self.controller.synth_loops) 
        self.bass_loop_index = self.find_index(None, self.controller.bass_loops)
        self.build_up_index = self.find_index(None, self.controller.build_ups)
        self.bass_hit_index = self.find_index(None, self.controller.bass_hits)
        self.snare_loop_index = self.find_index(None, self.controller.snare_loops)
        self.fx_hit_index = self.find_index(None, self.controller.fx_hits)
        self.background_loop_index = self.find_index(None, self.controller.background_loops)
        #self.perc_loop_index = self.find_index(None, self.controller.perc_loops)

    def find_index(self, key, music_list):
                
        selected_list = []

        for obj in music_list:
            
            if obj.bpm == 0:
                selected_list.append(obj)
            elif obj.bpm == self.bpm and key == None:
                selected_list.append(obj)
            elif key != None:
                if obj.key == key:
                    selected_list.append(obj)

        #deal with not repeating samples later        

        index = music_list.index(random.choice(selected_list))

        #indexes.append(index)
        return index
    