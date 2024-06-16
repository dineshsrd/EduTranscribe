import vosk
import sys
import os
import wave
import json

def transcribe(file_name):

    if not os.path.exists("model"):
        print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit (1)

    wf = wave.open(file_name, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    model = vosk.Model("model")
    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    transcript = ''
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            transcript += json.loads(rec.Result())["text"] + " "

        # else:
        #     transcript += rec.PartialResult()["text"] + " "
    transcript += json.loads(rec.FinalResult())["text"] + " "

    return transcript



