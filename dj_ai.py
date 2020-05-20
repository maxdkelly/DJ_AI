import random
import time
from routine import Routine

class DJ_AI():
    def __init__(self, sample_controller):
        self.controller = sample_controller

        self.func_list = [self.routine_A, self.routine_B, self.routine_C, self.routine_D]
        self.bpm_list = [120, 123, 125, 126, 127, 128, 130]
        self.set_list = []

    def create_set(self, length):

        for i in range(length):
            func = random.choice(self.func_list)
            bpm = random.choice(self.bpm_list)

            self.set_list.append((func,Routine(bpm,self.controller)))

    def play(self):

        for sequence in self.set_list:

            sequence[0](sequence[1])

    def routine_A(self, routine):
 
        print("Playing: Routine_A, BPM: " + str(routine.bpm))

        self.controller.start_bass_hit(routine.bass_hit_index,False) 
        self.controller.start_drums_tops(routine.drum_tops_index,False)
        time.sleep(16)
        self.controller.start_synth_loop(routine.synth_index,False)
        self.controller.stop_background_loop(True)
        time.sleep(16)
        self.controller.stop_drums_tops(False)
        self.controller.start_drums_full(routine.drum_full_index,True)
        time.sleep(18)
        self.controller.stop_drums_full(False)
        time.sleep(7)
        self.controller.stop_synth_loop(False)
        self.controller.start_bass_hit(routine.bass_hit_index,False) 
        self.controller.start_drums_full(routine.drum_full_index,False)
        self.controller.start_drums_tops(routine.drum_tops_index,True) 
        time.sleep(16)  
        self.controller.start_bass_loop(routine.bass_loop_index,False) 
        time.sleep(12)
        self.controller.stop_drums_tops(False)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index,False) 
        time.sleep(4)
        self.controller.start_drums_full(routine.drum_full_index_2,False)
        time.sleep(6)
        self.controller.stop_drums_tops(False)
        time.sleep(12)
        self.controller.stop_bass_loop(False)
        time.sleep(12)
        self.controller.start_snare_loop(routine.snare_loop_index,False)
        time.sleep(12)
        self.controller.stop_drums_full(False)
        time.sleep(6)
        self.controller.stop_snare_loop(False)
        
        
    def routine_B(self, routine):

        print("Playing: Routine_B, BPM: " + str(routine.bpm))

        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.start_drums_full(routine.drum_full_index,False)
        time.sleep(6)
        self.controller.start_fx_hit(routine.fx_hit_index,False)
        time.sleep(6)
        self.controller.start_fx_hit(routine.fx_hit_index,False)
        time.sleep(6)
        self.controller.start_bass_loop(routine.bass_loop_index,False)
        self.controller.stop_background_loop(True)
        time.sleep(18)
        self.controller.start_drums_tops(routine.drum_tops_index,True)
        self.controller.stop_drums_full(True)
        time.sleep(16)
        self.controller.stop_drums_tops(False)
        self.controller.start_drums_full(routine.drum_full_index,True)
        time.sleep(12)
        self.controller.stop_drums_full(False)
        time.sleep(12)   
        self.controller.start_drums_full(routine.drum_full_index_2,False)
        time.sleep(10)
        self.controller.stop_bass_loop(False)
        time.sleep(10)
        self.controller.start_synth_loop(routine.synth_index,False)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index,False)
        self.controller.stop_drums_full(True)
        time.sleep(12)
        self.controller.stop_synth_loop(False)
        time.sleep(14)
        self.controller.start_drums_full(routine.drum_full_index_2,False)
        time.sleep(18)
        self.controller.stop_drums_full(False)
        time.sleep(6)
        self.controller.start_drums_full(routine.drum_full_index,False)
        time.sleep(18)
        self.controller.stop_drums_tops(False)
        time.sleep(12)
        self.controller.build_up_transition(routine.build_up_index,False)
        self.controller.stop_drums_full(True)

    def routine_C(self, routine):

        print("Playing: Routine_C, BPM: " + str(routine.bpm))

        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.start_drums_full(routine.drum_full_index,False)
        time.sleep(12)
        self.controller.start_synth_loop(routine.synth_index,True)
        time.sleep(12)
        self.controller.stop_drums_full(False)
        time.sleep(16)
        self.controller.start_snare_loop(routine.snare_loop_index,False)
        time.sleep(12)
        self.controller.stop_snare_loop(False)
        self.controller.start_drums_full(routine.drum_full_index_2,True)
        time.sleep(12)
        self.controller.stop_drums_full(False)
        time.sleep(2)
        self.controller.start_drums_full(routine.drum_full_index,False)
        self.controller.start_bass_hit(routine.bass_hit_index,True)
        time.sleep(6)
        self.controller.stop_synth_loop(False)
        time.sleep(4)
        self.controller.start_bass_loop(routine.bass_loop_index,True)
        self.controller.start_background_loop(routine.background_loop_index,True)
        time.sleep(16)
        self.controller.stop_drums_full(False) 
        time.sleep(12)
        self.controller.stop_bass_loop(False)
        time.sleep(12)
       
    def routine_D(self, routine):

        print("Playing: Routine_D, BPM: " + str(routine.bpm))

        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.start_drums_full(routine.drum_full_index,False)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index,False)
        time.sleep(12)
        self.controller.stop_drums_tops(False)
        time.sleep(6)
        self.controller.start_drums_tops(routine.drum_tops_index_2,False)
        time.sleep(12)
        self.controller.stop_drums_full(False)
        time.sleep(12)
        self.controller.start_drums_full(routine.drum_full_index_2,False)
        time.sleep(12)
        self.controller.start_bass_loop(routine.bass_loop_index,False)
        self.controller.stop_drums_full(True)
        time.sleep(12)
        self.controller.stop_drums_tops(False)
        self.controller.start_drums_full(routine.drum_full_index_2,True)
        time.sleep(22)
        self.controller.stop_drums_full(False)
        time.sleep(12)
        self.controller.start_drums_full(routine.drum_full_index,False)
        self.controller.start_drums_tops(routine.drum_tops_index,True)
        time.sleep(12)
        self.controller.stop_bass_loop(False)
        self.controller.start_drums_tops(routine.drum_tops_index_2,True)
        time.sleep(12)
        self.controller.start_bass_loop(routine.bass_loop_index_2,False)
        self.controller.stop_drums_tops(True)
        time.sleep(22)
        self.controller.stop_drums_full(False)
        time.sleep(12)
        self.controller.stop_bass_loop(False)
        self.controller.start_bass_hit(routine.bass_hit_index,True)
        self.controller.start_drums_full(routine.drum_full_index_2,True)
        self.controller.start_drums_tops(routine.drum_tops_index,True)
        time.sleep(12)



        