import pygame
import time

#drums_full_channel = 0
#bass_channel = 1
#synth_channel = 2
#perc_channel = 3
#sounds_channel/vocal  = 4
#snare_channel = 5
#drum_tops_channel = 6


class Sample_Controller():

    def __init__(self, d_f, d_t, s_l, b_l, p_l, b_h, s_h, f_h, b_u, snare, back, i, v, t_t, f_t):
        self.drums_full = d_f
        self.drums_tops = d_t
        self.synth_loops = s_l
        self.bass_loops = b_l
        self.perc_loops = p_l
        self.bass_hits = b_h
        self.synth_hits = s_h
        self.fx_hits = f_h
        self.build_ups = b_u
        self.snare_loops = snare
        self.background_loops = back
        self.intro = i
        self.vocal_loops = v
        self.top_trans = t_t
        self.full_trans = f_t



        self.curr_drums_full_obj = None
        self.curr_drums_tops_obj = None  
        self.curr_synth_obj = None
        self.curr_bass_obj = None
        self.curr_snare_obj = None
        self.curr_vocal_obj = None
        self.curr_background_obj = None
        self.curr_trans_obj = None

        pygame.mixer.init()


    def wait_beat(self,now):

        if now:
            return

        if self.curr_synth_obj != None:
            self.curr_synth_obj.wait_loop()
        elif self.curr_bass_obj != None:
            self.curr_bass_obj.wait_loop()
        elif self.curr_drums_full_obj != None:
            self.curr_drums_full_obj.wait_loop()
        elif self.curr_drums_tops_obj != None:
            self.curr_drums_tops_obj.wait_loop()
        elif self.curr_vocal_obj != None:
            self.curr_vocal_obj.wait_loop()
        


    def play_intro(self,pos,now):
        self.wait_beat(now)
        print("Playing: " + self.intro[pos].path)
        pygame.mixer.Channel(4).play(pygame.mixer.Sound(self.intro[pos].path))
        time.sleep(self.intro[pos].length)

    def play_hit(self,sample,now,fade_length):

        self.wait_beat(now)  
        if fade_length == 0:
            print("Playing: " + sample.path)
        else:
            print("Playing: " + sample.path + ", Fade_In_Length: " + str(round(fade_length * sample.length,2)) + "s")

        pygame.mixer.Channel(4).play(pygame.mixer.Sound(sample.path), fade_ms = int(fade_length * sample.length * 1000))


    def play_loop(self,channel,sample, fade_length): 

        if sample.length >= 29:
            fade_length = fade_length/4

        if fade_length == 0:
            print("Playing: " + sample.path)
        else:
            print("Playing: " + sample.path + ", Fade_In_Length: " + str(round(fade_length * sample.length,2)) + "s")
     
        fade = int(fade_length * sample.length * 1000)
        pygame.mixer.Channel(channel).set_volume(1.0)
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(sample.path), loops = -1, fade_ms = fade)
        sample.start_loop()

    def stop_loop(self,channel,sample,fade_length):

        if sample == None:
            return

        if sample.length >= 29:
            fade_length = fade_length/4

        if fade_length == 0:
            print("Stopping: " + sample.path)
        else:
            print("Stopping: " + sample.path + ", Fade_Out_Length: " + str(round(fade_length * sample.length,2)) + "s")

        if fade_length == 0:
            pygame.mixer.Channel(channel).stop()
        else:
            fade = int(fade_length * sample.length * 1000)
            pygame.mixer.Channel(channel).fadeout(fade)  

    def isolate_element(self,elem):
        
        if self.curr_bass_obj != None and self.curr_bass_obj != elem:
            self.stop_bass_loop(False,1)
        if self.curr_drums_full_obj != None and self.curr_drums_full_obj != elem:
            self.stop_drums_full(False,1)
        if self.curr_drums_tops_obj != None and self.curr_drums_tops_obj != elem:
            self.stop_drums_tops(False,1)
        if self.curr_synth_obj != None and self.curr_synth_obj != elem:
            self.stop_synth_loop(False,1)
        if self.curr_snare_obj != None and self.curr_snare_obj != elem:
            self.stop_snare_loop(False,1)
        if self.curr_vocal_obj != None and self.curr_vocal_obj != elem:
            self.stop_vocal_loop(False,1)

    def build_up_transition(self,build_up_pos,now):

        sample = self.build_ups[build_up_pos]
        if self.curr_synth_obj != None:
            self.curr_synth_obj.wait_loop()
            if self.curr_synth_obj.length > sample.length:
                time.sleep(self.curr_synth_obj.length - sample.length)
        elif self.curr_bass_obj != None:
            self.curr_bass_obj.wait_loop()
            if self.curr_bass_obj.length > sample.length:
                time.sleep(self.curr_bass_obj.length - sample.length)
        else:
            self.wait_beat(now)
        
        print("Playing: "+ sample.path)
        pygame.mixer.Channel(5).play(pygame.mixer.Sound(sample.path), fade_ms = int(0.5 * sample.length * 1000))
        time.sleep(sample.length)

    def start_drums_full(self,pos,now,fade):

        self.wait_beat(now)
        self.play_loop(0,self.drums_full[pos],fade)
        self.curr_drums_full_obj = self.drums_full[pos]

    def start_drums_tops(self, pos, now, fade):
  
        self.wait_beat(now)
        self.play_loop(6,self.drums_tops[pos],fade)
        self.curr_drums_tops_obj = self.drums_tops[pos]

    def stop_drums_full(self,now,fade):

        self.wait_beat(now)
        self.stop_loop(0,self.curr_drums_full_obj,fade)
        self.curr_drums_full_obj = None

    def stop_drums_tops(self,now,fade):

        self.wait_beat(now)
        self.stop_loop(6,self.curr_drums_tops_obj,fade)
        self.curr_drums_tops_obj = None
       
    def start_bass_loop(self,pos,now, fade):

        self.wait_beat(now)
        self.play_loop(1,self.bass_loops[pos], fade)
        self.curr_bass_obj = self.bass_loops[pos]

    def stop_bass_loop(self,now, fade):

        self.wait_beat(now)
        self.stop_loop(1,self.curr_bass_obj,fade)
        self.curr_bass_obj = None

    def start_vocal_loop(self,pos,now, fade):

        self.wait_beat(now)
        self.play_loop(4,self.vocal_loops[pos], fade)
        self.curr_vocal_obj = self.vocal_loops[pos]

    def stop_vocal_loop(self,now, fade):

        self.wait_beat(now)
        self.stop_loop(4,self.curr_vocal_obj,fade)
        self.curr_vocal_obj = None

    def start_synth_loop(self,pos,now, fade):

        self.wait_beat(now)
 
        self.play_loop(2,self.synth_loops[pos],fade)
        self.curr_synth_obj = self.synth_loops[pos]
        
    def stop_synth_loop(self,now,fade):

        self.wait_beat(now)
        self.stop_loop(2,self.curr_synth_obj,fade)
        self.curr_synth_obj = None

    def start_bass_hit(self,pos,now):
        self.play_hit(self.bass_hits[pos],now,0)

    def start_synth_hit(self,pos,now):
        self.play_hit(self.synth_hits[pos],now,0)

    def start_fx_hit(self,pos,now):
        self.play_hit(self.fx_hits[pos],now,0)

    def start_top_trans(self,pos,now,fade):
        self.play_hit(self.top_trans[pos],now,fade)
        self.curr_trans_obj = self.top_trans[pos]

    def start_full_trans(self,pos,now,fade):
        self.play_hit(self.full_trans[pos],now,fade)
        self.curr_trans_obj = self.full_trans[pos]

    def stop_trans(self,now,fade):
        self.wait_beat(now)
        self.stop_loop(4,self.curr_trans_obj,fade)
        self.curr_synth_obj = None

    def start_background_loop(self,pos,now, fade):
        self.wait_beat(now)
        self.play_loop(7,self.background_loops[pos], fade)
        self.curr_background_obj = self.background_loops[pos] 

    def stop_background_loop(self,now,fade):
        self.wait_beat(now)
        self.stop_loop(7,self.curr_background_obj,fade)
        self.curr_background_obj = None

    def start_snare_loop(self,pos,now, fade):
        self.wait_beat(now)
        self.play_loop(5,self.snare_loops[pos], fade)
        self.curr_snare_obj = self.snare_loops[pos]

    def stop_snare_loop(self,now,fade):
        self.wait_beat(now)
        self.stop_loop(5,self.curr_snare_obj,fade)
        self.curr_snare_obj = None


    

    

       


