import random
import time
from routine import Routine

class DJ_AI():
    def __init__(self, sample_controller):
        self.controller = sample_controller

        self.func_list = [self.routine_A, self.routine_B, self.routine_C, self.routine_D, self.routine_E, self.routine_F]
        self.bpm_list = [120, 123, 125, 126, 127, 128, 130]
        self.set_list = []

    def create_set(self, length):

        for i in range(length):
            func = random.choice(self.func_list)
            bpm = random.choice(self.bpm_list)

            self.set_list.append((func,Routine(bpm,self.controller)))

    def play(self):

        self.play_intro()

        for sequence in self.set_list:
            sequence[0](sequence[1])

        self.closing_routine(Routine(random.choice(self.bpm_list),self.controller))

        self.play_intro()

    def play_intro(self):

        self.controller.play_intro(0,True)


    def routine_A(self, routine):
 
        print("Playing: Routine_A, BPM: " + str(routine.bpm))

        self.controller.start_bass_hit(routine.bass_hit_index,False) 
        self.controller.start_drums_tops(routine.drum_tops_index,False,0)
        time.sleep(16)
        self.controller.start_synth_loop(routine.synth_index,False,6)
        self.controller.stop_background_loop(True,0.1)
        time.sleep(16)
        self.controller.stop_drums_tops(False,0)
        self.controller.start_drums_full(routine.drum_full_index,True,0)
        time.sleep(18)
        self.controller.stop_drums_full(False,2)
        time.sleep(22)
        self.controller.stop_synth_loop(False,0)
        self.controller.start_bass_hit(routine.bass_hit_index,False) 
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        self.controller.start_drums_tops(routine.drum_tops_index,True,0) 
        time.sleep(16)  
        self.controller.start_bass_loop(routine.bass_loop_index,False,4) 
        time.sleep(12)
        self.controller.stop_drums_tops(False,0)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index,False,2) 
        time.sleep(4)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        time.sleep(6)
        self.controller.stop_drums_tops(False,2)
        time.sleep(12)
        self.controller.stop_bass_loop(False,4)
        time.sleep(12)
        self.controller.start_snare_loop(routine.snare_loop_index,False,0.3)
        time.sleep(6)
        self.controller.stop_drums_full(False,1)
        time.sleep(6)
        self.controller.stop_snare_loop(False,0)
        
        
    def routine_B(self, routine):

        print("Playing: Routine_B, BPM: " + str(routine.bpm))

        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        time.sleep(6)
        self.controller.start_fx_hit(routine.fx_hit_index,False)
        time.sleep(6)
        self.controller.start_fx_hit(routine.fx_hit_index,False)
        time.sleep(6)
        self.controller.start_bass_loop(routine.bass_loop_index,False,6)
        self.controller.stop_background_loop(True,0.1)
        time.sleep(18)
        self.controller.start_drums_tops(routine.drum_tops_index,True,0)
        self.controller.stop_drums_full(True,0)
        time.sleep(16)
        self.controller.stop_drums_tops(False,0)
        self.controller.start_drums_full(routine.drum_full_index,True,0)
        time.sleep(12)
        self.controller.stop_drums_full(False,2)
        time.sleep(12)   
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        time.sleep(10)
        self.controller.stop_bass_loop(False,6)
        time.sleep(10)
        self.controller.start_synth_loop(routine.synth_index,False,6)
        time.sleep(16)
        self.controller.start_drums_tops(routine.drum_tops_index,False,0)
        self.controller.stop_drums_full(True,0)
        time.sleep(16)
        self.controller.stop_synth_loop(False,3)
        time.sleep(14)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        time.sleep(18)
        self.controller.stop_drums_full(False,2)
        time.sleep(6)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        time.sleep(18)
        self.controller.stop_drums_tops(False,2)
        time.sleep(12)
        self.controller.build_up_transition(routine.build_up_index,False)
        self.controller.stop_drums_full(True,0)

    def routine_C(self, routine):

        print("Playing: Routine_C, BPM: " + str(routine.bpm))

        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        time.sleep(22)
        self.controller.start_synth_loop(routine.synth_index,False,8)
        self.controller.stop_background_loop(True,0.1)
        time.sleep(12)
        self.controller.stop_drums_full(False,2)
        time.sleep(16)
        self.controller.start_snare_loop(routine.snare_loop_index,False,0.4)
        time.sleep(12)
        self.controller.stop_snare_loop(False,0)
        self.controller.start_drums_full(routine.drum_full_index_2,True,0)
        time.sleep(12)
        self.controller.stop_drums_full(False,2)
        time.sleep(6)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        self.controller.start_bass_hit(routine.bass_hit_index,True)
        self.controller.stop_synth_loop(True,0)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index_2,False,2)
        time.sleep(6)
        self.controller.stop_drums_full(False,2)
        self.controller.start_bass_loop(routine.bass_loop_index,True,4)
        self.controller.start_background_loop(routine.background_loop_index,True,0)
        time.sleep(16)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        self.controller.stop_drums_tops(True,0)
        time.sleep(22)
        self.controller.stop_drums_full(False,6) 
        time.sleep(16)
        self.controller.stop_bass_loop(False,4)
        time.sleep(22)
       
    def routine_D(self, routine):

        print("Playing: Routine_D, BPM: " + str(routine.bpm))

        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index,False,2)
        self.controller.stop_background_loop(True,0.1)
        time.sleep(16)
        self.controller.stop_drums_tops(False,0)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index_2,False,2)
        time.sleep(16)
        self.controller.stop_drums_full(False,2)
        time.sleep(16)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        time.sleep(12)
        self.controller.start_bass_loop(routine.bass_loop_index,False,2)
        self.controller.stop_drums_full(True,2)
        time.sleep(16)
        self.controller.stop_drums_tops(False,0)
        self.controller.start_drums_full(routine.drum_full_index_2,True,0)
        time.sleep(22)
        self.controller.stop_drums_full(False,2)
        time.sleep(12)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        self.controller.start_drums_tops(routine.drum_tops_index,True,0)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index_2,False,0)
        time.sleep(2)
        self.controller.stop_bass_loop(False,6)
        time.sleep(16)
        self.controller.start_bass_loop(routine.bass_loop_index_2,False,4)
        self.controller.stop_drums_tops(True,0)
        time.sleep(22)
        self.controller.stop_drums_full(False,2)
        time.sleep(12)
        self.controller.stop_bass_loop(False,0)
        self.controller.start_bass_hit(routine.bass_hit_index,True)
        self.controller.start_drums_full(routine.drum_full_index_2,True,0)
        self.controller.start_drums_tops(routine.drum_tops_index,True,0)
        time.sleep(6)
        self.controller.start_bass_hit(routine.bass_hit_index,False)
        time.sleep(6)
        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.stop_drums_tops(True,0)
        time.sleep(6)
        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.start_bass_loop(routine.bass_loop_index,True,2)
        time.sleep(6)
        self.controller.stop_drums_full(False,2)
        time.sleep(12)
        self.controller.build_up_transition(routine.build_up_index,False)
        self.controller.stop_bass_loop(True,0)

    def routine_E(self, routine):

        print("Playing: Routine_E, BPM: " + str(routine.bpm))

        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        time.sleep(16)
        self.controller.start_bass_loop(routine.bass_loop_index,False,5)
        self.controller.stop_background_loop(True,0.1)
        time.sleep(16)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        time.sleep(16)
        self.controller.stop_bass_loop(False,6)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index,False,4)
        time.sleep(18)
        self.controller.stop_drums_full(False,2)
        time.sleep(16)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        time.sleep(12)
        self.controller.start_bass_loop(routine.bass_loop_index_2,False,0)
        self.controller.stop_drums_tops(True,0)
        time.sleep(22)
        self.controller.stop_bass_loop(False,6)
        time.sleep(22)
        self.controller.start_synth_loop(routine.synth_index,False,8)
        time.sleep(22)
        self.controller.start_drums_tops(routine.drum_tops_index_2,False,0)
        time.sleep(6)
        self.controller.stop_drums_full(False,2)
        time.sleep(12)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        self.controller.stop_drums_tops(True,0)
        time.sleep(16)
        self.controller.stop_drums_full(True,4)
        time.sleep(12)
        self.controller.build_up_transition(routine.build_up_index,False)
        self.controller.stop_synth_loop(True,0)

    def routine_F(self, routine):

        print("Playing: Routine_F, BPM: " + str(routine.bpm))

        self.controller.start_drums_full(routine.drum_full_index,False,0)
        self.controller.stop_background_loop(True,0)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index,False,4)
        time.sleep(16)
        self.controller.stop_drums_full(False,1)
        time.sleep(16)
        self.controller.start_drums_full(routine.drum_full_index_2,False,4)
        time.sleep(22)
        self.controller.start_bass_loop(routine.bass_loop_index,False,0)
        self.controller.stop_drums_tops(True,0)
        time.sleep(16)
        self.controller.stop_drums_full(False,2)
        time.sleep(16)
        self.controller.start_snare_loop(routine.snare_loop_index,False,0.7)
        time.sleep(16)
        self.controller.stop_snare_loop(False,0)
        self.controller.start_drums_full(routine.drum_full_index_2,True,0)
        time.sleep(8)
        self.controller.start_drums_tops(routine.drum_tops_index_2,False,2)
        time.sleep(12)
        self.controller.stop_drums_full(False,2)
        time.sleep(12)
        self.controller.stop_bass_loop(False,4)
        time.sleep(18)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        time.sleep(16)
        self.controller.start_synth_loop(routine.synth_index,False,8)
        time.sleep(12)
        self.controller.stop_drums_tops(False,0)
        time.sleep(16)
        self.controller.stop_drums_full(False,4)
        time.sleep(12)
        self.controller.start_snare_loop(routine.snare_loop_index,False,0.5)
        time.sleep(16)
        self.controller.stop_snare_loop(False,0)
        self.controller.stop_synth_loop(True,0)
        

        
    def closing_routine(self, routine):

        print("Playing: Closing_Routine, BPM: " + str(routine.bpm))

        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        time.sleep(16)
        self.controller.start_bass_loop(routine.bass_loop_index,False,5)
        self.controller.stop_background_loop(True,0)
        time.sleep(16)
        self.controller.start_drums_tops(routine.drum_tops_index,False,0)
        time.sleep(12)
        self.controller.stop_drums_tops(False,6)   
        time.sleep(22)
        self.controller.stop_drums_full(False,6)
        time.sleep(22)
        self.controller.stop_bass_loop(False,4)
        time.sleep(22)




        
