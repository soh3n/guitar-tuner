import pyaudio
import aubio
import numpy as num
import numpy
import simpleaudio

notes = {
    1: ["A" ,440.0],
    2: ["A#",466.2],
    3: ["B" ,493.9],
    4: ["C" ,523.3],
    5: ["C#",554.4],
    6: ["D" ,587.3],
    7: ["D#",622.3],
    8: ["E" ,659.3],
    9: ["F" ,698.5],
    10:["F#",740.0],
    11:["G" ,784.0],
    12:["G#",830.6],
}

def play(note, sec):
    octave = 4

    frequency = (int)(notes[1]) * 2 ** (((octave * 12) - 48)  / 12)
    fs = 44100
    seconds = sec

    t = numpy.linspace(0, seconds, seconds * fs, False)

    note = numpy.sin(frequency * t * 2 * numpy.pi)

    audio = note * (2**15 - 1) / numpy.max(numpy.abs(note))
    audio = audio.astype(numpy.int16)

    play_obj = simpleaudio.play_buffer(audio, 1, 2, fs)


enter = input("Enter 1 to start recording.\nEnter 2 to generate tone given a note.\n")

if enter == "1":
    seconds = int(input("Enter time in seconds you'd like to record: "))
    pitch = pyaudio.PyAudio()

    stream = pitch.open(format=pyaudio.paFloat32,
    channels=1, rate=44100, input=True,
    frames_per_buffer=1024)

    pitchDetect = aubio.pitch("default", 2048,
    2048//2, 44100)

    for i in range(seconds):
        data = stream.read(1024)
        samples = num.frombuffer(data,
        dtype=aubio.float_type)
        p = pitchDetect(samples)[0]
        print(p)

if enter == "2":
    note = input("Enter note you'd like to hear: ")
    sec = input("Enter time in seconds you'd like it to last: ")

    play(note, sec)