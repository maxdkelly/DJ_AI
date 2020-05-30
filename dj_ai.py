import random
import time
from routine import Routine

class DJ_AI():
    def __init__(self, sample_controller):
        self.controller = sample_controller

        self.func_list = [self.routine_A, self.routine_B, self.routine_C, self.routine_D, self.routine_E, self.routine_F]
        self.bpm_list = [120, 123, 125, 126, 127, 128, 130]
        self.set_list = []

        self.rout_list = []
        self.rout_list.append(self.bass_routine)
        self.rout_list.append(self.bass_routine_2)
        self.rout_list.append(self.bass_snare_routine)
        self.rout_list.append(self.synth_routine)
        self.rout_list.append(self.synth_routine_2)
        self.rout_list.append(self.synth_snare_routine)
        self.rout_list.append(self.drums_full_top_routine)
        self.rout_list.append(self.vocal_routine)
        self.rout_list.append(self.synth_bass_routine)
        self.rout_list.append(self.synth_bass_routine_2)

        self.routines = []

    def create_function_list(self):

        routine_list = []

        for i in range(3):

            rout = random.choice(self.rout_list)
            while rout in routine_list:
                rout = random.choice(self.rout_list)

            routine_list.append(rout)

        return routine_list

    def append_set(self, function_list, full, end):

        for x in function_list:

            self.set_list.append(x)

        if not end:
            if full == 'Full':
                self.set_list.append((self.full_transition_routine))
            else:
                self.set_list.append((self.top_transition_routine))


    def generate_routines(self,length):

        bpm = random.choice(self.bpm_list)
        curr_routine = Routine(bpm,self.controller)

        self.routines.append(curr_routine)

        if length != 1:
            self.append_set(self.create_function_list(),curr_routine.trans_option,False)
        else:
            self.append_set(self.create_function_list(),curr_routine.trans_option,True)

        self.function_list = []

        for i in range(length - 1):

            if curr_routine.trans_option == 'Full':
                new_routine = Routine(curr_routine.end_bpm_full, self.controller)
            else:
                new_routine = Routine(curr_routine.end_bpm_top, self.controller)


            self.routines.append(new_routine)
            curr_routine = new_routine

            if i == length - 2:
                self.append_set(self.create_function_list(),curr_routine.trans_option,True)
            else:
                self.append_set(self.create_function_list(),curr_routine.trans_option,False)

        

        

    def create_set(self, length):

        for i in range(length):
            func = random.choice(self.func_list)
            bpm = random.choice(self.bpm_list)

            self.set_list.append((func,Routine(bpm,self.controller)))

    def play(self):

       # self.play_intro()

        rout_i = 0
        for routine in self.set_list:

            if routine != self.top_transition_routine and routine != self.full_transition_routine:
                routine(self.routines[rout_i])
            else:
                routine(self.routines[rout_i],self.routines[rout_i + 1])
                rout_i = rout_i + 1

        self.closing_routine()
        self.play_intro()


   

    def play_intro(self):

        self.controller.play_intro(0,True)


    def top_transition_routine(self, routine_1, routine_2):

        if self.controller.curr_drums_full_obj == None:
            self.controller.start_drums_full(routine_1.drum_full_index,False,0)
            time.sleep(6)
        self.controller.isolate_element(self.controller.curr_drums_full_obj)
        time.sleep(12)
        self.controller.start_top_trans(routine_1.top_trans_index,False,0.3)
        time.sleep(10)
        self.controller.stop_drums_full(False,1)
        time.sleep(20)
        self.controller.start_drums_full(routine_2.drum_full_index,False,1)
        time.sleep(6)
        self.controller.stop_trans(False,0.5)
        time.sleep(12)

    def full_transition_routine(self, routine_1, routine_2):

        if self.controller.curr_drums_tops_obj == None:
            self.controller.start_drums_tops(routine_1.drum_tops_index,False,1)
            time.sleep(6)
        self.controller.isolate_element(self.controller.curr_drums_tops_obj)
        time.sleep(12)
        self.controller.start_full_trans(routine_1.full_trans_index,False,0)
        time.sleep(10)
        self.controller.stop_drums_tops(False,1)
        time.sleep(20)
        self.controller.start_drums_tops(routine_2.drum_tops_index,False,1)
        time.sleep(6)
        self.controller.stop_trans(False,0.5)
        time.sleep(12)

    def synth_snare_routine(self, routine):
        if self.controller.curr_drums_full_obj == None:
            self.controller.start_drums_full(routine.drum_full_index_2,False,0)
            time.sleep(6)
        self.controller.isolate_element(self.controller.curr_drums_full_obj)
        time.sleep(12)
        self.controller.start_synth_loop(routine.synth_index,False,14)
        time.sleep(16)
        self.controller.stop_drums_full(False,5)
        time.sleep(22)
        self.controller.start_snare_loop(routine.snare_loop_index,False,1.2)
        time.sleep(26)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        self.controller.stop_snare_loop(True,0)
        time.sleep(16)
        self.controller.stop_synth_loop(False,3)
        time.sleep(22)

    def synth_routine_2(self, routine):
        if self.controller.curr_drums_full_obj == None:
            self.controller.start_drums_full(routine.drum_full_index_2,False,0)
            time.sleep(6)
        self.controller.isolate_element(self.controller.curr_drums_full_obj)
        time.sleep(12)
        self.controller.start_synth_loop(routine.synth_index,False,12)
        self.controller.stop_drums_full(True,8)
        time.sleep(56)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        time.sleep(16)
        self.controller.stop_synth_loop(False,2)
        time.sleep(16)

    def synth_routine(self, routine):
        if self.controller.curr_drums_tops_obj == None:
            self.controller.start_drums_tops(routine.drum_tops_index_2,False,2)
            time.sleep(12)
        self.controller.isolate_element(self.controller.curr_drums_tops_obj)
        time.sleep(12)
        self.controller.start_synth_loop(routine.synth_index_2,False,10)
        self.controller.stop_drums_tops(True,8)
        time.sleep(76)
        self.controller.stop_synth_loop(False,0)
        self.controller.start_drums_full(routine.drum_full_index,True,0)
        self.controller.start_drums_tops(routine.drum_tops_index,True,0)
        self.controller.start_bass_hit(routine.bass_hit_index,True)
        time.sleep(32)

    def bass_routine(self, routine):
        if self.controller.curr_drums_full_obj == None:
            self.controller.start_drums_full(routine.drum_full_index,False,2)
            time.sleep(12)
        self.controller.isolate_element(self.controller.curr_drums_full_obj)
        time.sleep(16)
        self.controller.start_drums_tops(routine.drum_tops_index,False,5)
        time.sleep(12)
        self.controller.stop_drums_full(False,5)
        self.controller.start_bass_loop(routine.bass_loop_index,False,4)
        time.sleep(46)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        self.controller.stop_drums_tops(True,0)
        time.sleep(22)
        self.controller.stop_bass_loop(False,4)
        time.sleep(22)

    def bass_routine_2(self, routine):
        if self.controller.curr_drums_full_obj == None:
            self.controller.start_drums_full(routine.drum_full_index_2,False,2)
            time.sleep(12)
        self.controller.isolate_element(self.controller.curr_drums_full_obj)
        time.sleep(12)
        self.controller.start_bass_loop(routine.bass_loop_index_2,False,10)
        self.controller.stop_drums_full(False,6)
        time.sleep(66)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        self.controller.start_drums_tops(routine.drum_tops_index,True,0)
        time.sleep(22)
        self.controller.stop_bass_loop(False,3)
        time.sleep(22)


    def bass_snare_routine(self, routine):
        if self.controller.curr_drums_tops_obj == None:
            self.controller.start_drums_tops(routine.drum_tops_index,False,2)
            time.sleep(12)
        self.controller.isolate_element(self.controller.curr_drums_tops_obj)
        time.sleep(12)
        self.controller.start_bass_loop(routine.bass_loop_index_2,False,10)
        time.sleep(6)
        self.controller.stop_drums_tops(False,5)
        time.sleep(46)
        self.controller.build_up_transition(routine.build_up_index,False)
        self.controller.start_drums_full(routine.drum_full_index,True,0)
        time.sleep(22)
        self.controller.stop_bass_loop(False,4)
        time.sleep(16)

    def synth_bass_routine(self, routine):
        if self.controller.curr_drums_tops_obj == None:
            self.controller.start_drums_tops(routine.drum_tops_index,False,2)
            time.sleep(12)
        self.controller.isolate_element(self.controller.curr_drums_tops_obj)
        time.sleep(6)
        self.controller.start_bass_loop(routine.bass_pair_index,False,4)
        time.sleep(32)
        self.controller.stop_bass_loop(False,5)
        self.controller.start_synth_loop(routine.synth_pair_index,True,5)
        time.sleep(62)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        self.controller.start_bass_loop(routine.bass_pair_index,True,0)
        self.controller.stop_drums_tops(True,0)
        time.sleep(12)
        self.controller.stop_synth_loop(False,2)
        time.sleep(16)
        self.controller.stop_bass_loop(False,2)
        time.sleep(16)

    def synth_bass_routine_2(self, routine):
        if self.controller.curr_synth_obj == None:
            self.controller.start_synth_loop(routine.synth_pair_index,False,4)
            time.sleep(12)
        self.controller.isolate_element(self.controller.curr_synth_obj)
        time.sleep(12)
        self.controller.start_bass_loop(routine.bass_pair_index,False,4)
        time.sleep(22)
        self.controller.start_drums_tops(routine.drum_tops_index,False,6)
        time.sleep(22)
        self.controller.stop_synth_loop(False,4)
        time.sleep(32)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        self.controller.stop_drums_tops(True,0)
        time.sleep(22)
    
    def drums_full_top_routine(self, routine):

        if self.controller.curr_drums_full_obj == None:
            self.controller.start_drums_full(routine.drum_full_index,False,0)
            time.sleep(6)
        self.controller.isolate_element(self.controller.curr_drums_full_obj)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index,False,14)
        time.sleep(26)
        self.controller.stop_drums_full(False,5)
        time.sleep(46)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        time.sleep(22)

    def vocal_routine(self, routine):
        if self.controller.curr_drums_tops_obj == None:
            self.controller.start_drums_tops(routine.drum_tops_index,False,2)
            time.sleep(12)
        self.controller.isolate_element(self.controller.curr_drums_tops_obj)
        time.sleep(6)
        self.controller.start_bass_loop(routine.bass_loop_index_2,False,5)
        time.sleep(22)
        self.controller.start_vocal_loop(routine.vocal_loop_index,False,4)
        self.controller.stop_bass_loop(True,5)
        time.sleep(46)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        self.controller.stop_drums_tops(True,0)
        time.sleep(22)
        self.controller.stop_vocal_loop(False,2)
        time.sleep(16)

    

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
        time.sleep(22)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)  
        time.sleep(8)
        self.controller.stop_synth_loop(False,3)
        time.sleep(18)
        self.controller.stop_drums_full(False,2)
        time.sleep(12)
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
        time.sleep(16)
        self.controller.stop_drums_full(False,2)
        time.sleep(12)
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
        time.sleep(22)
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
        self.controller.stop_bass_loop(False,4)
        self.controller.start_drums_tops(routine.drum_tops_index,True,4)
        time.sleep(12)
        self.controller.start_drums_full(routine.drum_full_index_2,True,0)
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

        self.controller.start_bass_hit(routine.bass_hit_index,False)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        self.controller.stop_background_loop(True,0)
        time.sleep(12)
        self.controller.start_drums_tops(routine.drum_tops_index,False,4)
        time.sleep(16)
        self.controller.stop_drums_full(False,1)
        time.sleep(16)
        self.controller.start_drums_full(routine.drum_full_index_2,False,0)
        time.sleep(22)
        self.controller.start_bass_loop(routine.bass_loop_index,False,1)
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
        self.controller.stop_bass_loop(False,3)
        time.sleep(18)
        self.controller.start_drums_full(routine.drum_full_index,False,0)
        time.sleep(16)
        self.controller.start_synth_loop(routine.synth_index,False,5)
        time.sleep(12)
        self.controller.stop_drums_tops(False,0)
        time.sleep(16)
        self.controller.stop_drums_full(False,4)
        time.sleep(12)
        self.controller.start_snare_loop(routine.snare_loop_index,False,0.7)
        time.sleep(16)
        self.controller.stop_snare_loop(False,0)
        self.controller.stop_synth_loop(True,0)
        

    

 
        
    def closing_routine(self):

        self.controller.isolate_element(self.controller.curr_drums_full_obj)
        time.sleep(6)
        self.controller.stop_drums_full(False,6)
        time.sleep(12)

        




        
