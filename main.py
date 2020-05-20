from os import listdir
from os.path import isfile, join
import time
import pygame

from sample import Sample
from drums import Drums
from synth import Synth
from bass import Bass
from percussion import Percussion
from fx import FX
from sample_controller import Sample_Controller
from routine import Routine
from dj_ai import DJ_AI

def create_samples(my_path,func):

    only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    samples = []

    for file in only_files:
        sample_obj = func(file,my_path)
        samples.append(sample_obj)

    return samples

def create_drum(file,my_path):
    split_str = file.split('_')
    print(split_str)
    bpm = int(split_str[1])
    wav = my_path + "/" + file

    return Drums(bpm, wav)

def create_synth(file,my_path):
    split_str = file.split('_')
    print(split_str)
    bpm = int(split_str[1])
    key = split_str[2]
    wav = my_path + "/" + file

    return Synth(bpm, key, wav)

def create_bass(file,my_path):
    split_str = file.split('_')
    print(split_str)
    bpm = int(split_str[1])
    key = split_str[2]
    wav = my_path + "/" + file

    return Bass(bpm, key, wav)

def create_perc(file,my_path):
    split_str = file.split('_')
    print(split_str)
    bpm = int(split_str[1])
    wav = my_path + "/" + file

    return Percussion(bpm, wav)

def create_fx(file,my_path):
    split_str = file.split('_')
    print(split_str)
    bpm = int(split_str[1])
    wav = my_path + "/" + file

    return FX(bpm, wav)


if __name__ == "__main__":
   
    drums_full = create_samples("Samples/Loops/Drums/Full",create_drum)
    drums_tops = create_samples("Samples/Loops/Drums/Tops",create_drum)
    synth_loops = create_samples("Samples/Loops/Synths",create_synth)
    bass_loops = create_samples("Samples/Loops/Bass",create_bass)
    perc_loops = create_samples("Samples/Loops/Percussion",create_perc)
    snare_loops = create_samples("Samples/Loops/Snares",create_drum)
    background = create_samples("Samples/Loops/Background",create_fx)

    bass_hits = create_samples("Samples/Sounds/Bass",create_bass)
    synth_hits = create_samples("Samples/Sounds/Synths",create_synth)
    fx_hits = create_samples("Samples/Sounds/FX",create_fx)
    
    build_ups = create_samples("Samples/Sounds/Build_Ups",create_drum)
    

    controller = Sample_Controller(drums_full,drums_tops,synth_loops,bass_loops,perc_loops,bass_hits, synth_hits,fx_hits,build_ups,snare_loops,background)

    dj = DJ_AI(controller)

    dj.create_set(4)
    dj.play()

   # routine_one = Routine(127,controller)
    #routine_two = Routine(120,controller)
    #routine_three = Routine(125,controller)

    #dj.routine_A(routine_three)
    #dj.routine_C(routine_two)
    #dj.routine_D(routine_one)
    
    
    

    
    
    
    





