import pygame
import time

#drums_channel = 0
#bass_channel = 1
#synth_channel = 2
#perc_channel = 3

#sounds_channel = 4

#snare_channel = 5


class Sample_Controller():

    def __init__(self, d_f, d_t, s_l, b_l, p_l, b_h, s_h, f_h, b_u, snare, back, i):
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

        self.curr_drums_full_obj = None
        self.curr_drums_tops_obj = None  
        self.curr_synth_obj = None
        self.curr_bass_obj = None

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
        


    def play_intro(self,pos,now):
        self.wait_beat(now)
        print("Playing: " + self.intro[pos].path)
        pygame.mixer.Channel(4).play(pygame.mixer.Sound(self.intro[pos].path))
        time.sleep(self.intro[pos].length)

    def play_hit(self,sample,now):

        self.wait_beat(now)  
        print("Playing: " + sample.path)
        pygame.mixer.Channel(4).play(pygame.mixer.Sound(sample.path))


    def play_loop(self,channel,sample, fade_length): 
        print("Playing: " + sample.path)

        fade = int(fade_length * sample.length * 1000)
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(sample.path), loops = -1, fade_ms = fade)
        sample.start_loop()

    def build_up_transition(self,build_up_pos,now):
        self.wait_beat(now)
        sample = self.build_ups[build_up_pos]
        print("Playing: "+ sample.path)
        pygame.mixer.Channel(5).play(pygame.mixer.Sound(sample.path))
        self.curr_drums_full_obj = None
        self.curr_drums_tops_obj = None
        time.sleep(sample.length)

        #self.curr_synth_obj = None
        #self.stop_synth_loop()


    def start_drums_full(self,pos,now,fade):

        self.wait_beat(now)
        self.play_loop(0,self.drums_full[pos],fade)
        self.curr_drums_full_obj = self.drums_full[pos]

    def start_drums_tops(self, pos, now, fade):
  
        self.wait_beat(now)
        self.play_loop(6,self.drums_tops[pos],fade)
        self.curr_drums_tops_obj = self.drums_tops[pos]

    def stop_drums_full(self,now):

        self.wait_beat(now)
        print("Stopping: Drum Full Track")
        pygame.mixer.Channel(0).stop()
        self.curr_drums_full_obj = None

    def stop_drums_tops(self,now):

        self.wait_beat(now)
        print("Stopping: Drum Tops Track")
        pygame.mixer.Channel(6).stop()

        self.curr_drums_tops_obj = None
       
    def start_bass_loop(self,pos,now, fade):

        self.wait_beat(now)
        self.play_loop(1,self.bass_loops[pos], fade)
        self.curr_bass_obj = self.bass_loops[pos]

    def stop_bass_loop(self,now):

        self.wait_beat(now)
        print("Stopping: Bass Track")
        pygame.mixer.Channel(1).stop()
        self.curr_bass_obj = None

    def start_synth_loop(self,pos,now, fade):

        self.wait_beat(now)
 
        self.play_loop(2,self.synth_loops[pos],fade)
        self.curr_synth_obj = self.synth_loops[pos]
        
    def stop_synth_loop(self,now):

        self.wait_beat(now)
        print("Stopping: Synth Track")
        pygame.mixer.Channel(2).stop()
        self.curr_synth_obj = None

    def start_perc_loop(self,pos,now, fade):
  
        self.wait_beat(now)
        self.play_loop(3,self.perc_loops[pos], fade)
        
    def stop_perc_loop(self,now):
        self.wait_beat(now)
        print("Stopping: Percussion Track")
        pygame.mixer.Channel(3).stop()

    def start_bass_hit(self,pos,now):
        self.play_hit(self.bass_hits[pos],now)

    def start_synth_hit(self,pos,now):
        self.play_hit(self.synth_hits[pos],now)

    def start_fx_hit(self,pos,now):
        self.play_hit(self.fx_hits[pos],now)

    def start_background_loop(self,pos,now, fade):
        self.wait_beat(now)
        self.play_loop(7,self.background_loops[pos], fade)

    def stop_background_loop(self,now):
        self.wait_beat(now)
        print("Stopping: Background Track")
        pygame.mixer.Channel(7).stop()

    def start_snare_loop(self,pos,now, fade):
        self.wait_beat(now)
        self.play_loop(5,self.snare_loops[pos], fade)

    def stop_snare_loop(self,now):
        self.wait_beat(now)
        print("Stopping: Snare Track")
        pygame.mixer.Channel(5).stop()


    

    

       


