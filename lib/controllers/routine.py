import random
import time
from lib.controllers.camelot import Camelot

class Routine():

    def __init__(self, bpm, controller):

        self.bpm = bpm
        self.controller = controller
        self.trans_option = random.choice(['Full', 'Tops', 'Tops'])

        self.drum_full_index = self.find_index(self.controller.drums_full)
        self.drum_full_index_2 = self.find_index(self.controller.drums_full)
        self.drum_tops_index = self.find_index(self.controller.drums_tops)
        self.drum_tops_index_2 = self.find_index(self.controller.drums_tops)
        self.synth_index = self.find_index(self.controller.synth_loops)
        self.synth_index_2 = self.find_index(self.controller.synth_loops) 
        self.bass_loop_index = self.find_index(self.controller.bass_loops)
        self.bass_loop_index_2 = self.find_index(self.controller.bass_loops)
        self.build_up_index = self.find_index(self.controller.build_ups)
        self.bass_hit_index = self.find_index(self.controller.bass_hits)
        self.snare_loop_index = self.find_index(self.controller.snare_loops)
        self.fx_hit_index = self.find_index(self.controller.fx_hits)
        self.fx_hit_index_2 = self.find_index(self.controller.fx_hits)
        self.background_loop_index = self.find_index(self.controller.background_loops)
        self.intro_index = self.find_index(self.controller.intro)
        self.vocal_loop_index = self.find_index(self.controller.vocal_loops)
        self.perc_loop_index = self.find_index(self.controller.perc_loops)

        self.top_trans_index = self.find_trans(self.controller.top_trans)
        self.full_trans_index = self.find_trans(self.controller.full_trans)

        self.end_bpm_top = self.controller.top_trans[self.top_trans_index].end_bpm
        self.end_bpm_full = self.controller.full_trans[self.full_trans_index].end_bpm

        self.synth_pair_index = None
        self.bass_pair_index = None

        cam_wheel = Camelot()

        self.bass_to_synth_index = self.find_index(self.controller.bass_loops) 
        self.synth_index_end = cam_wheel.find_samples(self.controller.bass_loops[self.bass_to_synth_index],self.controller.synth_loops)
        while self.synth_index_end == -1:
            self.bass_to_synth_index = self.find_index(self.controller.bass_loops) 
            self.synth_index_end = cam_wheel.find_samples(self.controller.bass_loops[self.bass_to_synth_index],self.controller.synth_loops)

        self.bass_index_start = self.find_index(self.controller.bass_loops) 
        self.bass_index_end = cam_wheel.find_samples(self.controller.bass_loops[self.bass_index_start],self.controller.bass_loops)
        while self.bass_index_end == -1:
            self.bass_index_start = self.find_index(self.controller.bass_loops) 
            self.bass_index_end = cam_wheel.find_samples(self.controller.bass_loops[self.bass_index_start],self.controller.bass_loops)

        self.synth_1 = self.find_index(self.controller.synth_loops) 
        self.synth_2 = cam_wheel.find_samples(self.controller.synth_loops[self.synth_1],self.controller.synth_loops)
        while self.synth_2 == -1:
            self.synth_1 = self.find_index(self.controller.synth_loops) 
            self.synth_2 = cam_wheel.find_samples(self.controller.synth_loops[self.synth_1],self.controller.synth_loops)
     
        self.find_synth_bass(self.controller.synth_loops,self.controller.bass_loops)


    def find_trans(self, music_list):

        selected_list = []

        for obj in music_list:
            
            if obj.start_bpm == self.bpm:
                selected_list.append(obj)
        
        choice = random.choice(selected_list)

        return music_list.index(choice)

    def find_synth_bass(self, music_list_1, music_list_2):

        selected_list = []

        for obj in music_list_1:
            if obj.bpm == self.bpm:
                for obj_2 in music_list_2:
                    if obj_2.bpm == self.bpm and obj_2.key == obj.key:
                        selected_list.append((obj,obj_2))

        choice = random.choice(selected_list)

        self.synth_pair_index = music_list_1.index(choice[0])
        self.bass_pair_index = music_list_2.index(choice[1])
        
    def find_index(self, music_list):
                
        selected_list = []

        for obj in music_list:
            
            if obj.bpm == 0:
                selected_list.append(obj)
            elif obj.bpm == self.bpm:
                selected_list.append(obj)

        if not selected_list:
            return -1        

        return music_list.index(random.choice(selected_list))

        
    